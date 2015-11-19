//This function draws cluster transition visualizations
function cluster_transitions(data) {
	"use strict";
  /*sets up the canvas for the visualization*/
	var margin = 75,
	width = content_width,
	height = 700 - margin;

	var y = d3.scale.linear()
					.range([height,0]);

	var x_left = d3.scale.ordinal()
		  				 .rangeRoundBands([0, width], .1);

	var x_middle = d3.scale.ordinal()
		  				   .rangeRoundBands([0, width], .1);

	var x_right = d3.scale.ordinal()
		  				  .rangeRoundBands([0, width], .1); 

	var colors = d3.scale.category10();

	var xAxis_left = d3.svg.axis()
				  	   .scale(x_left)
	    		       .orient("bottom");

	var xAxis_middle = d3.svg.axis()
				         .scale(x_middle)
	    		         .orient("bottom");

	var xAxis_right = d3.svg.axis()
				  		.scale(x_right)
	    		  		.orient("bottom");

	var yAxis = d3.svg.axis()
				  .scale(y)
				  .orient("left");

	//Adds the SVG element that will house everything else
	var svg = d3.select("body")
				.append("svg")
				.attr("id", "svg_transitions")
				.attr("width", width + margin)
				.attr("height", height + margin);

	function update_transitions_chart(cluster_sol){
		//cluster_sol is a number that indicates the solution number of the central cluster
		num_observations = data.length;
		var previous_cluster_sol = d3.nest()
									 .key(function(d){return d[(cluster_sol-1)+"_cluster"];})
									 .rollup(function(leaves){
									 	var responses = leaves.length;
									 	return {
									 		'responses': responses,
									 		'percent': responses/num_observations
									 	};  
									 })
									 .entries(data);
		
		var current_cluster_sol = d3.nest()
									 .key(function(d){return d[(cluster_sol)+"_cluster"];})
									 .rollup(function(leaves){
									 	var responses = leaves.length;
									 	return {
									 		'responses': responses,
									 		'percent': responses/num_observations
									 	};  
									 })
									 .entries(data);
		
		var next_cluster_sol = d3.nest()
									 .key(function(d){return d[(cluster_sol+1)+"_cluster"];})
									 .rollup(function(leaves){
									 	var responses = leaves.length;
									 	return {
									 		'total' : total,
									 		'responses': responses,
									 		'percent': responses/num_observations
									 	};  
									 })
									 .entries(data);
		debugger;
		x_left.domain(previous_cluster_sol.map(function(d) {
												return d.total;
											   }))

	}
}