draw_diagram="""
function draw_diagram() {
    var svg1 = d3.select("#svg1");
    svg1.append("circle")
           .attr("cx",100)
           .attr("cy", 100)
           .attr("r", 90)
           .attr("fill", "red");
    var svg2 = d3.select("#svg2");
    svg2.append("circle")
           .attr("cx",100)
           .attr("cy", 100)
           .attr("r", 90)
           .attr("fill", "blue");
}
"""
