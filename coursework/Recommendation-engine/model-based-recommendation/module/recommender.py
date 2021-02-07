import numpy as np
import pandas as pd
import recommender_functions as rf
import sys # can use sys to take command line arguments


class Recommender:
    '''
    What is this class all about - write a really good doc string here
    '''
    def __init__(self):
        '''
        what do we need to start out our recommender system

        INPUTS: None
        OUTPUTS: None
        '''

    def fit(self, movie_path, review_path, latent_factors=5, learning_rate=0.0001, iters=100):

        '''
        fit the recommender to your dataset and also have this save the results
        to pull from when you need to make predictions

        INPUTS:
            movie_path: a file path to movie data (str)
            review_path: a file path to review data (str)
            latent_factors: number of latent features, default to 5 (int)
            learning_rate: learning rate for gradient descent, default to 0.0001 (float),
                the higher, the faster it may fit but the higher the risk of diversion
                the lower, the slower but it is more likely to converge
            iters: number of iterations of gradient descent, default to 100 (int)
                too lower number of iterations may result in convergence failure

        OUTPUTS:
            user_mat: a matrix of number of users x number of latent factors (numpy.ndarray)
            movie_mat a matrix of number of latent x factors number of movies (numpy.ndarray)
        '''
        self.movies = pd.read_csv(movie_path)
        self.reviews = pd.read_csv(review_path)

        # Create user_movie_matrix
        user_movie = self.reviews[['user_id', 'movie_id', 'rating']]
        self.user_movie_df = user_movie.groupby(['user_id', 'movie_id'])['rating'].max().unstack()
        self.user_movie_matrix = np.array(self.user_movie_df)

        # List of all existing users and movies
        self.user_ids_series = np.array(self.user_movie_df.index)
        self.movie_ids_series = np.array(self.user_movie_df.columns)

        # Set up values for FunkSVD
        self.iters = iters
        self.learning_rate = learning_rate
        self.latent_factors = latent_factors
        self.n_users = self.user_movie_df.shape[0]
        self.n_movies = self.user_movie_df.shape[1]
        self.num_rating = np.count_nonzero(~np.isnan(self.user_movie_matrix))
        sse = 0

        # Instantiate matrices w/ random values
        user_mat = np.random.random((self.n_users, self.latent_factors))  # n_users * n_latent_factors
        movie_mat = np.random.random((self.latent_factors, self.n_users))  # n_latent_factors * n_movies

        # Train FunkSVD
        print('Fitting FunkSVD...🚀')
        print("Iterations | Mean Squared Error ")

        for iteration in range(iters):

            # Initialize sum squared errors for each iteration
            old_sse = sse
            sse = 0

            for i in range(self.n_users):
                for j in range(self.n_movies):
                    # Check if value exists
                    if self.user_movie_matrix[i, j] > 0:
                        act = self.user_movie_matrix[i, j]
                        pred = np.dot(user_mat[i, :], movie_mat[:, j])

                        diff = act - pred
                        sse += diff ** 2

                        # Gradient descent and update user_mat, movie_mat

                        for k in range(self.latent_factors):
                            user_mat[i, k] += self.learning_rate * (2*diff*movie_mat[k, j])
                            movie_mat[k, j] += self.learning_rate * (2*diff*user_mat[i, k])

            # Print results
            print(f'{ iteration+1 } \t\t { sse / self.num_rating }')

        # SVD based fit
        # Keep user_mat and movie_mat for safe keeping
        self.user_mat = user_mat
        self.movie_mat = movie_mat

        # Knowledge based fit (for non-existing users)
        self.ranked_movies = rf.create_ranked_df(self.movies, self.reviews)


    def predict_rating(self, user_id, movie_id):
        '''
        makes predictions of a rating for a user on a movie-user combo
        using the result of the fitted FunkSVD

        Note that user_id and movie_id must exist in the original dataset
        in order to get the predicted rating. Otherwise, knowledge-based
        recommendation may be used for general recommendations, which is
        however outside the scope of this function

        INPUTS:
            user_id: the id of a specific user of interest (int)
            movie_id: the movie of a specific movie of interest (int)
        OUTPUT:
            pred: the predicted rating for user-movie of interest (float)
        '''

        try:
            user_idx = np.where(self.user_ids_series == user_id)[0][0]
            movie_idx = np.where(self.movie_ids_series == movie_id)[0][0]

            # Take a dot product of U, V for prediciton
            pred = np.dot(self.user_mat[user_idx, :], self.movie_mat[:, movie_idx])

            # Print message
            movie_title = self.movies[self.movies['movie_id'] == movie_id]['movie'].values[0]
            print(f'For user {user_id!r}, the predicted rating for {movie_title!r} is {pred:.2f}')

            return pred

        except:
            print(f'Prediction can be made from your inputs. It looks that '
                  f'either user_id {user_id!r} or movie_id {movie_id!r} does not exist in our database')
            return None

    def make_recs(self, _id, _id_type='user', num_recs=5):
        '''
        given a user id or a movie that an individual likes
        make recommendations

        INPUTS:
            _id: the id of user or movie (int)
            _id_type: the type of category that the id falls into: user or movie,
                default to user (str)
            num_recs: int, number of recommendation to show, default to 5  (int)
        OUTPUTS:
            rec_ids: a list of ids of recommended movies (list)
            rec_names: a list of recommended movies by number of num_recs parameter (list)
        '''

        # Instantiate outputs
        rec_ids = list()
        rec_names = list()

        if _id_type == 'user':
            if _id in self.user_ids_series:
                # Find the index of user
                user_idx = np.where(self.user_ids_series == _id)[0][0]

                # Make predictions
                preds = np.dot(self.user_mat[user_idx, :], self.movie_mat)  # 1 x num_movies matrix

                # Sort by the highest rating
                indices = preds.argsort()[-num_recs:][::-1]
                rec_ids = list(self.user_ids_series[indices])
                rec_names = rf.get_movie_names(rec_ids, self.movies)

            else:
                print(f'Could not find user {_id}, so we are recommending the most popular movies in general.')
                rec_names = rf.popular_recommendations(_id, num_recs, self.ranked_movies)

        elif _id_type == 'movie':
            if _id in self.movie_ids_series:
                rec_names = list(rf.find_similar_movies(_id, self.movies))

        # Fill rec_ids it not exist
        if not len(rec_ids) > 0:
            rec_ids = [self.movies[self.movies['movie'] == title]['movie_id'].values[0] for title in rec_names]

        else:
            print('Invalid _id_type')

        return rec_ids, rec_names


if __name__ == '__main__':
    # test different parts to make sure it works
    import recommender as r

    # Instantiate Recommender class
    rec = r.Recommender()

    # Fit recommender
    rec.fit(review_path='./data/train_data.csv', movie_path='./data/movies_clean.csv', learning_rate=.01, iters=1)

    # predict
    rec.predict_rating(user_id=8, movie_id=2844)

    # make recommendations
    print(rec.make_recs(8, 'user')) # user in the dataset
    print(rec.make_recs(1, 'user')) # user not in dataset
    print(rec.make_recs(1853728)) # movie in the dataset
    print(rec.make_recs(1)) # movie not in dataset
    print(rec.n_users)
    print(rec.n_movies)
    print(rec.num_rating)




