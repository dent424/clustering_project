//This function draws cluster transition visualizations
function cluster_transitions(data) {
	"use strict";
  /*sets up the canvas for the visualization*/
	var content_width = 1000;

	var margin = 75,
	width = content_width,
	height = 700 - margin;

	var breakout_width = width*0.1;

	var y = d3.scale.linear()
					.range([height,0]);

	var x_left = d3.scale.ordinal()
		  				 .rangeRoundBands([0, breakout_width], .1);

	var x_middle = d3.scale.ordinal()
		  				   .rangeRoundBands([0, breakout_width], .1);

	var x_right = d3.scale.ordinal()
		  				  .rangeRoundBands([0, breakout_width], .1); 

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
		var y0 = y(0)
		var y1 = 0
		var num_observations = data.length;
		var previous_cluster_sol = d3.nest()
									 .key(function(d){return d[(cluster_sol-1)+"_clusters"];})
									 .rollup(function(leaves){
									 	var responses = leaves.length;
									 	var percent = responses/num_observations;
									 	y0 = y1;
									 	y1 = y(0) + y0 - y(percent); 
									 	return {
									 		'cluster_num' : leaves[0][(cluster_sol-1)+"_clusters"],
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
									 	var percent = responses/num_observations;
									 	y0 = y1;
									 	y1 = y(0) + y0 - y(percent); 
									 	return {
									 		'cluster_num' : leaves[0][(cluster_sol)+"_clusters"],
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
		var next_cluster_sol = d3.nest()
									 .key(function(d){return d[(cluster_sol+1)+"_clusters"];})
									 .rollup(function(leaves){
									 	var responses = leaves.length;
									 	var percent = responses/num_observations;
									 	y0 = y1;
									 	y1 = y(0) + y0 - y(percent); 
									 	return {
									 		'cluster_num' : leaves[0][(cluster_sol+1)+"_clusters"],
									 		'total' : num_observations,
									 		'responses': responses,
									 		'percent': percent,
									 		'y0': y0,
									 		'y1': y1
									 	};  
									 })
									 .entries(data);

		x_left.domain(previous_cluster_sol.map(function(d) {
												return d.total;
											   }));


		

		//create g to hold bars
		var left_group = svg.selectAll('.left_bars')
					   .data(previous_cluster_sol, function(d) {return d.key;});

		var center_group = svg.selectAll('.center_bars')
					   .data(current_cluster_sol, function(d) {return d.key;});

		var right_group = svg.selectAll('.right_bars')
					   .data(next_cluster_sol, function(d) {return d.key;});

		//remove bars
		var exitbars_left = left_group.exit();
		exitbars_left.remove();

		var exitbars_center = center_group.exit();
		exitbars_center.remove();

		var exitbars_right = right_group.exit();
		exitbars_right.remove();


		//Enter selection
		var entergroup_left = left_group.enter()
						  				.append('g')
						  				.attr('class','left_bars')
						  				.attr('id',function(d){
						  					return d.values['cluster_num']
						  				});

		var entergroup_center = center_group.enter()
											.append('g')
						  					.attr('class','center_bars')
						  					.attr('id',function(d){
						  						return d.values['cluster_num']
						  					})
						  					.attr('transform','translate('+(content_width/2-breakout_width/2)+',0)');

		var entergroup_right = right_group.enter()
											.append('g')
						  					.attr('class','right_bars')
						  					.attr('id',function(d){
						  						return d.values['cluster_num']
						  					})
						  					.attr('transform','translate('+(content_width-breakout_width)+',0)');


		entergroup_left.append('rect')
				  	   .attr('width', x_left.rangeBand())
				  	   .attr('class','transition_rect');

		entergroup_center.append('rect')
				  		.attr('width', x_left.rangeBand())
				  		.attr('class','transition_rect');

		entergroup_right.append('rect')
				  		.attr('width', x_left.rangeBand())
				  		.attr('class','transition_rect');

		//update left rects
		left_group.select('rect')
				  .attr('height', function(d) {
				  	return height - y(+d.values['percent'].toPrecision(3));
				  })
				  .attr('y', function(d){
				  	return d.values['y0'];
				  })
				  .style('fill', function(d){
				  	return colors(d.values['cluster_num']);
				  });

		center_group.select('rect')
		  .attr('height', function(d) {
		  	return height - y(+d.values['percent'].toPrecision(3));
		  })
		  .attr('y', function(d){
		  	return d.values['y0'];
		  })
		  .style('fill', function(d){
		  	return colors(d.values['cluster_num']);
		  });

		right_group.select('rect')
		  .attr('height', function(d) {
		  	return height - y(+d.values['percent'].toPrecision(3));
		  })
		  .attr('y', function(d){
		  	return d.values['y0'];
		  })
		  .style('fill', function(d){
		  	return colors(d.values['cluster_num']);
		  });

		svg.select('g.xAxis_left')
		   .call(xAxis_left);

		svg.select('g.yAxis')
		   .call(yAxis);
	}
	update_transitions_chart(5);
}