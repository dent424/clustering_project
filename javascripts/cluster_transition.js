//This function draws cluster transition visualizations
function cluster_transitions(data) {
	"use strict";
  /*sets up the canvas for the visualization*/
	var content_width = 1000;

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

	;
	function update_transitions_chart(cluster_sol){
		//cluster_sol is a number that indicates the solution number of the central cluster
		colors.domain();
		y.domain([0,1.1])
		var y0 = 0
		var y1 = 0
		var num_observations = data.length;
		var previous_cluster_sol = d3.nest()
									 .key(function(d){return d[(cluster_sol-1)+"_clusters"];})
									 .rollup(function(leaves){
									 	var responses = leaves.length;
									 	var percent = responses/num_observations;
									 	y0 = y1;
									 	y1 = y0 + y(percent); 
									 	return {
									 		'total' : num_observations,
									 		'responses': responses,
									 		'percent': percent,
									 		'y0': y0,
									 		'y1': y1
									 	};  
									 })
									 .entries(data);
		
		y0 = 0;
		y1 = 0;
		var current_cluster_sol = d3.nest()
									 .key(function(d){return d[(cluster_sol)+"_clusters"];})
									 .rollup(function(leaves){
									 	var responses = leaves.length;
									 	return {
									 		'total' : num_observations,
									 		'responses': responses,
									 		'percent': responses/num_observations
									 	};  
									 })
									 .entries(data);
		y0 = 0;
		y1 = 0;
		var next_cluster_sol = d3.nest()
									 .key(function(d){return d[(cluster_sol+1)+"_clusters"];})
									 .rollup(function(leaves){
									 	var responses = leaves.length;
									 	return {
									 		'total' : num_observations,
									 		'responses': responses,
									 		'percent': responses/num_observations
									 	};  
									 })
									 .entries(data);

		x_left.domain(previous_cluster_sol.map(function(d) {
												return d.total;
											   }));


		

		//create g to hold bars on left
		var left_group = svg.selectAll('.left_bars')
					   .data(previous_cluster_sol, function(d) {return d.key;});

		//remove left bars
		var exitbars = left_group.exit();
		exitbars.remove();

		//Enter left selection
		var entergroup = left_group.enter()
						  .append('g')
						  .attr('class','left_bars');

		entergroup.append('rect')
				  .attr('width', x_left.rangeBand())
				  .attr('class','transition_rect');

		//update left rects
		left_group.select('rect')
				  .attr('height', function(d) {
				  	return y(+d.values['percent'].toPrecision(3));
				  })
				  .attr('y', function(d){
				  	return d.values['y0'];
				  })
				  .style('fill', function(d){
				  	return colors(d.values['y0']);
				  });

		svg.select('g.xAxis_left')
		   .call(xAxis_left);

		svg.select('g.yAxis')
		   .call(yAxis);
	}
	update_transitions_chart(3);
}