// Lembre-se de substituir '/api/compare_execution_time' pelo caminho correto do endpoint
d3.json('/api/compare_execution_time')
    .then(data => {
        const margin = {top: 20, right: 20, bottom: 30, left: 40},
            width = 960 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        const x = d3.scaleBand()
            .range([0, width])
            .padding(0.1);
        const y = d3.scaleLinear()
            .range([height, 0]);

        const svg = d3.select("#execution-time-chart").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

        x.domain(data.map(function(d) { return d.label; }));
        y.domain([0, d3.max(data, function(d) { return d.value; })]);

        svg.selectAll(".bar")
            .data(data)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function(d) { return x(d.label); })
            .attr("width", x.bandwidth())
            .attr("y", function(d) { return y(d.value); })
            .attr("height", function(d) { return height - y(d.value); });

        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));

        svg.append("g")
            .call(d3.axisLeft(y));
    })
    .catch(error => {
        console.error("Error:", error);
    });