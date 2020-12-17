const period = [];

for (let i = 1995; i <= 2015; i++) {
    period.push(parseInt(i));
}

// Brazil
const arable_land_brz = [
    30.924583699244103,
    30.990028882024003,
    31.0554740648039,
    31.1207996037396,
    31.198209170939897,
    31.275618738140302,
    31.521965413357503,
    31.8094695709811,
    32.1206632097572,
    32.558918611078504,
    32.5948835506464,
    32.6369263974999,
    32.4998145520415,
    32.7225913899504,
    32.7273771437186,
    32.7181645677148,
    32.9466843101456,
    32.974680969689395,
    33.3576728793727,
    33.8100342899258,
    33.8100342899258,
];

const country_name_brz = 'Brazil';
const trace1 = {
    /* Construct a line chart 
    x : period, z: arable_land_brz */

    x: period,
    y: arable_land_brz,
    type: 'scatter',
    mode: 'lines+markers',
    name: country_name_brz,
    lines: {
        color: 'rgb(164, 194, 244)',
        width: 1,
    },
};

// Germany
const arable_land_ger = [
    49.67917502148379,
    49.6634105817984,
    49.6404526572124,
    49.776517105037,
    49.1489483638031,
    48.912451640636206,
    48.822012037833204,
    48.6355558103537,
    48.7400017201342,
    48.7799982796686,
    48.8330083725198,
    48.5948612066988,
    48.61330197608051,
    48.535696870607794,
    48.4380826711798,
    47.9100324181656,
    47.9659169153087,
    47.8108681930338,
    47.8588626461821,
    47.9363714531384,
    47.9592041483809,
];

const country_name_ger = 'Germany';
const trace2 = {
    x: period,
    y: arable_land_ger,
    type: 'scatter',
    mode: 'lines+markers',
    name: country_name_ger,
    lines: {
        color: 'rgb(255, 217, 102)',
        width: 1,
    },
};

// Republic of Korea
const arable_land_kor = [
    18.48434584,
    18.09040017,
    17.85195936,
    17.70682148,
    17.61351856,
    17.8104914,
    17.45916891,
    17.29517512,
    17.13842975,
    17.07291882,
    16.9643779,
    16.71139554,
    16.47750722,
    16.13568409,
    15.82526272,
    15.50411523,
    15.3102171,
    15.64279058,
    15.35319226,
    15.14933799,
    15.02899071,
];

const country_name_kor = 'Rep. Korea';
const trace3 = {
    x: period,
    y: arable_land_kor,
    type: 'scatter',
    mode: 'lines+markers',
    name: country_name_kor,
    lines: {
        color: 'rgb(142, 124, 195)',
        width: 1,
    },
};

const data = [trace1, trace2, trace3];

const layout = {
    title: 'Percent of Land Used for Agriculture <br> 1995-2015',
    // xaxis: {
    //     title: 'year',
    //     automargin: true,
    // },
    yaxis: {
        title: 'arable land (%)',
    },
    // width: '',
    // height: ''

    // Position legend in the center
    showlegend: true,
    legend: {
        orientation: 'v',
        // x: 0.5,
        // y: 1,
    },
};

Plotly.newPlot('plot1', data, layout);
