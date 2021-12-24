var margin = {top: 20, right: 20, bottom: 60, left: 80},
    width = 500 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;
var data = [
    {language: "Python", value: 30},
    {language: "Java", value: 20},
    {language: "C/C++", value: 15},
    {language: "Javascript", value: 35},
    {language: "PHP", value: 15},
];
colors = ["#00A5E3", "#FF96C5", "#00CDAC", "#FFA23A", "#74737A"];
var svg = d3
    .select("body") //create Svg element
    .append("svg")
    .attr("width", width + margin.right + margin.left)
    .attr("height", height + margin.top + margin.bottom)
    .style("border", "solid 1px red")
    .attr("transform", "translate(200,0)");
var chart = svg
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
    .attr("width", width)
    .attr("height", height);
var pie = d3.pie().value((d) => d.value);
var color_scale = d3
    .scaleOrdinal()
    .domain(data.map((d) => d.language))
    .range(colors);
let arc = d3.arc().outerRadius(150).innerRadius(0);
var p_chart = chart
    .selectAll("pie")
    .data(pie(data))
    .enter()
    .append("g")
    .attr("transform", "translate(170,230)");
p_chart
    .append("path")
    .attr("d", arc)
    .attr("fill", (d) => {
        return color_scale(d.data.language);
    });
p_chart
    .append("text")
    .text(function (d) {
        return d.data.language;
    })
    .attr("transform", function (d) {
        return "translate(" + arc.centroid(d) + ")";
    })
    .style("text-anchor", "middle");
