// Lembre-se de substituir '/api/update_big_o_plot' pelo caminho correto do endpoint
d3.json('/api/update_big_o_plot')
    .then(data => {
        const margin = {top: 20, right: 20, bottom: 30, left: 50},
            width = 960 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        const x = d3.scaleLinear().range([0, width]);
        const y = d3.scaleLinear().range([height, 0]);

        const line = d3.line()
            .x(function(d) { return x(d.number); })
            .y(function(d) { return y(d.time); });

        const svg = d3.select("#big-o-chart").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

        x.domain(d3.extent(data, function(d) { return d.number; }));
        y.domain([0, d3.max(data, function(d) { return d.time; })]);

        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        svg.append("g")
            .call(d3.axisLeft(y));

        svg.append("path")
            .data([data])
            .attr("class", "line")
            .attr("d", line);
    })
    .catch(error => {
        console.error("Error:", error);
    });
