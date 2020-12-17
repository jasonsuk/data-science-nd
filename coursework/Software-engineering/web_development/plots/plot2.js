const year = [2015];
const arable_land_brz_2015 = [33.8100342899258];
// const country_name_brz = 'Brazil';

const arable_land_ger_2015 = [47.9592041483809];
// const country_name_ger = 'Germany';

const arable_land_kor_2015 = [15.02899071];
// const country_name_kor = 'Rep. Korea';

const trace_p2 = {
    /* Construct a bar chart
    x: country_name y: arable_land*/
    x: [country_name_brz, country_name_ger, country_name_kor],
    y: [
        arable_land_brz_2015[0],
        arable_land_ger_2015[0],
        arable_land_kor_2015[0],
    ],
    type: 'bar',
    name: year[0],
    marker: {
        color: 'rgb(70, 124, 195)',
    },
};

const data_p2 = [trace_p2];

const layout_p2 = {
    // barmode: stack
    title: 'Percent of Land Used for Agriculture<br>in 2015',
    xaxis: {
        title: 'country',
    },
    yaxis: {
        title: 'arable land (%)',
    },
};

Plotly.newPlot('plot2', data_p2, layout_p2);
