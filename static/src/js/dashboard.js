odoo.define('engineers_management.DashboardRewrite', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var EngineerDashboard = AbstractAction.extend({
        template: 'EngineerDashboardMain',

        start: function () {
            // console.log("START FUNCTION")
            var self = this;
            return this._super().then(function () {
                self.render_department_employee();
                self.render_tooltip_template();
            });
        },

        render_department_employee: function () {
            // console.log("It works")
            // var self = this;
            var w = 300;
            var h = 300;
            var r = h / 2;
            var elem = this.$('.emp_graph');
            var colors = ['#70cac1', '#659d4e', '#208cc2', '#4d6cb1', '#584999', '#8e559e', '#cf3650', '#f65337', '#fe7139',
                '#ffa433', '#ffc25b', '#f8e54b'];
            var color = d3.scale.ordinal().range(colors);
            rpc.query({
                model: "hr.employee",
                method: "get_dept_employee",
            }).then(function (data) {
                var segColor = {};
                var vis = d3.select(elem[0]).append("svg:svg").data([data]).attr("width", w).attr("height", h).append("svg:g").attr("transform", "translate(" + r + "," + r + ")");
                var pie = d3.layout.pie().value(function (d) {
                    return d.value;
                });
                var arc = d3.svg.arc().outerRadius(r);
                var arcs = vis.selectAll("g.slice").data(pie).enter().append("svg:g").attr("class", "slice");
                arcs.append("svg:path")
                    .attr("fill", function (d, i) {
                        return color(i);
                    })
                    .attr("d", function (d) {
                        return arc(d);
                    });

                var legend = d3.select(elem[0]).append("table").attr('class', 'legend');

                // create one row per segment.
                var tr = legend.append("tbody").selectAll("tr").data(data).enter().append("tr");

                // create the first column for each segment.
                tr.append("td").append("svg").attr("width", '16').attr("height", '16').append("rect")
                    .attr("width", '16').attr("height", '16')
                    .attr("fill", function (d, i) {
                        return color(i)
                    });

                // create the second column for each segment.
                tr.append("td").text(function (d) {
                    return d.label;
                });

                // create the third column for each segment.
                tr.append("td").attr("class", 'legendFreq')
                    .text(function (d) {
                        return d.value;
                    });
            });
        },

        render_tooltip_template: function () {
            // console.log("It works");
            var margin = {top: 20, right: 25, bottom: 30, left: 40},
                width = 450 - margin.left - margin.right,
                height = 450 - margin.top - margin.bottom;
            var value = this.$('.div_template');
            // append the svg object to the body of the page
            var svg = d3.select(value[0])
                .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

            //Read the data
            d3.csv("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/heatmap_data.csv", function (data) {

                // Labels of row and columns -> unique identifier of the column called 'group' and 'variable'
                var myGroups = d3.map(data, function (d) {
                    return d.group;
                }).keys()
                var myVars = d3.map(data, function (d) {
                    return d.variable;
                }).keys()

                // Build X scales and axis:
                var x = d3.scaleBand()
                    .range([0, width])
                    .domain(myGroups)
                    .padding(0.05);
                svg.append("g")
                    .style("font-size", 15)
                    .attr("transform", "translate(0," + height + ")")
                    .call(d3.axisBottom(x).tickSize(0))
                    .select(".domain").remove()

                // Build Y scales and axis:
                var y = d3.scaleBand()
                    .range([height, 0])
                    .domain(myVars)
                    .padding(0.05);
                svg.append("g")
                    .style("font-size", 15)
                    .call(d3.axisLeft(y).tickSize(0))
                    .select(".domain").remove()

                // Build color scale
                var myColor = d3.scaleSequential()
                    .interpolator(d3.interpolateInferno)
                    .domain([1, 100])

                // create a tooltip
                var Tooltip = d3.select("#div_template")
                    .append("div")
                    .style("opacity", 0)
                    .attr("class", "tooltip")
                    .style("background-color", "white")
                    .style("border", "solid")
                    .style("border-width", "2px")
                    .style("border-radius", "5px")
                    .style("padding", "5px")

                // Three function that change the tooltip when user hover / move / leave a cell
                var mouseover = function (d) {
                    Tooltip
                        .style("opacity", 1)
                    d3.select(this)
                        .style("stroke", "black")
                        .style("opacity", 1)
                }
                var mousemove = function (d) {
                    Tooltip
                        .html("The exact value of<br>this cell is: " + d.value)
                        .style("left", (d3.mouse(this)[0] + 70) + "px")
                        .style("top", (d3.mouse(this)[1]) + "px")
                }
                var mouseleave = function (d) {
                    Tooltip
                        .style("opacity", 0)
                    d3.select(this)
                        .style("stroke", "none")
                        .style("opacity", 0.8)
                }

                // add the squares
                svg.selectAll()
                    .data(data, function (d) {
                        return d.group + ':' + d.variable;
                    })
                    .enter()
                    .append("rect")
                    .attr("x", function (d) {
                        return x(d.group)
                    })
                    .attr("y", function (d) {
                        return y(d.variable)
                    })
                    .attr("rx", 4)
                    .attr("ry", 4)
                    .attr("width", x.bandwidth())
                    .attr("height", y.bandwidth())
                    .style("fill", function (d) {
                        return myColor(d.value)
                    })
                    .style("stroke-width", 4)
                    .style("stroke", "none")
                    .style("opacity", 0.8)
                    .on("mouseover", mouseover)
                    .on("mousemove", mousemove)
                    .on("mouseleave", mouseleave)
            })
        },
    });

    core.action_registry.add('engineer_dashboard_tag', EngineerDashboard);
    return EngineerDashboard;

});