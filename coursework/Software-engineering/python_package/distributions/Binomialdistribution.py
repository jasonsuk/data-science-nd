import math
import matplotlib.pyplot as plt

from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring


    For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    You can then calculate the mean and standard deviation with the following formula:
        mean = p * n
        standard deviation = sqrt(n * p * (1 - p))                
    """

    def __init__(self, probability=0.5, size=20):

        self.p = probability
        self.n = size

        Distribution.__init__(self, self.calculate_mean(),
                              self.calculate_stdev())

    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args: 
            None

        Returns: 
            float: mean of the data set

        """

        self.mean = 1.0 * self.p * self.n

        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args: 
            None

        Returns: 
            float: standard deviation of the data set

        """

        self.stdev = math.sqrt(self.n * self.p * (1-self.p))

        return self.stdev

    def update_stats_with_data(self):
        """Function to calculate p and n from the data set. 
        The function updates the p and n variables of the object.

        Args: 
            None

        Returns: 
            float: the p value
            float: the n value

        """

        self.p = 1.0 * sum(self.data) / len(self.data)
        self.n = len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self):
        """Function to output a bar chart of the instance variable data 
        using matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.bar(x=['0', '1'], height=[self.n*(1-self.p), self.n*self.p])
        plt.title('Bar chart of data')
        plt.xlabel('outcome')
        plt.ylabel('count')

        plt.show()

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        coef = math.factorial(self.n) / (math.factorial(k) *
                                         math.factorial(self.n - k))
        prob = (self.p ** k) * ((1 - self.p) ** (self.n - k))

        return coef * prob

    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        x = []
        y = []

        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        plt.bar(x, y)
        plt.title('Distribution of outcome')
        plt.xlabel('outcome')
        plt.ylabel('probability')

        plt.show()

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        Remark: 
            p value for two binomial distributions must be same for this function
            The new n value is the sum of the n values of the two distributions.

        """

        # Check if two binomial distributions share the same p
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        Remark: 
            format : mean 5, standard deviation 4.5, p .8, n 20

        """

        return f'mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}'
