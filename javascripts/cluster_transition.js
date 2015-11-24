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
		function update_stacked_bars(cluster_sol){
			colors.domain();
			y.domain([0,1.1])
			var y0 = y(0)
			var y1 = 0
			var num_observations = data.length;
			var prev_cluster_counts = {}
			var previous_cluster_sol = d3.nest()
										 .key(function(d){return d[(cluster_sol-1)+"_clusters"];})
										 .rollup(function(leaves){
										 	var responses = leaves.length;
										 	var percent = responses/num_observations;
										 	var cluster_num = leaves[0][(cluster_sol-1)+"_clusters"];
										 	prev_cluster_counts[cluster_num] = responses;
										 	y0 = y1;
										 	y1 = y(0) + y0 - y(percent); 
										 	return {
										 		'cluster_num' : cluster_num,
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
			var current_cluster_counts = {}
			var current_cluster_sol = d3.nest()
										 .key(function(d){return d[(cluster_sol)+"_clusters"];})
										 .rollup(function(leaves){
										 	var responses = leaves.length;
										 	var percent = responses/num_observations;
										 	var cluster_num = leaves[0][(cluster_sol)+"_clusters"];
										 	current_cluster_counts[cluster_num] = responses;
										 	y0 = y1;
										 	y1 = y(0) + y0 - y(percent); 
										 	return {
										 		'cluster_num' : cluster_num,
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
			var next_cluster_counts = {}
			var next_cluster_sol = d3.nest()
										 .key(function(d){return d[(cluster_sol+1)+"_clusters"];})
										 .rollup(function(leaves){
										 	var responses = leaves.length;
										 	var percent = responses/num_observations;
											var cluster_num = leaves[0][(cluster_sol+1)+"_clusters"];
										 	next_cluster_counts[cluster_num] = responses;
										 	y0 = y1;
										 	y1 = y(0) + y0 - y(percent); 
										 	return {
										 		'cluster_num' : cluster_num,
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

			var output = {'total': num_observations,
						  'previous': prev_cluster_counts,
						  'current' : current_cluster_counts,
						  'next': next_cluster_counts}
			return output 

		}
		
		function update_bar_connectors(cluster_sol, cluster_info){
			var prev_current_connector = d3.nest()
							 			   .key(function(d){return d[(cluster_sol-1)+"_clusters"];})
							 			   .key(function(d){return d[cluster_sol+"_clusters"];})
							 			   .rollup(function(leaves){
											 	var num_observations = cluster_info['total']
											 	var responses = leaves.length;
											 	var percent_total = responses/num_observations;
											 	var prev_cluster_name = leaves[0][(cluster_sol-1)+"_clusters"];
											 	var current_cluster_name = leaves[0][(cluster_sol)+"_clusters"];
							 					var from_cluster_total = +cluster_info['previous'][prev_cluster_name];
							 					var to_cluster_total = +cluster_info['current'][current_cluster_name];
							 					return {
							 						'from_cluster' : prev_cluster_name,
							 						'to_cluster': current_cluster_name,
											 		'total' : num_observations,
											 		'responses': responses,
											 		'percent_of_total': percent_total,
											 		'from_cluster_total': from_cluster_total,
											 		'to_cluster_total' : to_cluster_total,
											 		'percent_of_from_cluster': responses/from_cluster_total,
											 		'percent_of_to_cluster': responses/to_cluster_total
											 	};  
							 				})
							 			   .entries(data);
			colors.domain();
			y.domain([0,1.1])
			x_left.domain(prev_current_connector.map(function(d) {
													return d.total;
												   }));

			//create g to hold transition lines
			var left_group = svg.selectAll('.left_transition_g')
						   .data(prev_current_connector, function(d) {return d.key;})
						   
			//debugger;
			//remove transition lines
			var exittrans_left = left_group.exit();
			exittrans_left.remove();

			//Enter selection
			var trans_entergroup_left = left_group.enter()
												  .append('g')
												  .selectAll('polygon')
												  .data(function(d) {
												  	//debugger;
												  	return d.values
												  })
												  .enter()
												  .append('polygon')
					  	   						  .attr('width', x_left.rangeBand())
					  	   						  .attr('class','transition_poly');

			//update left transitions
			left_group.select('polygon')
					  .attr('height', function(d) {
					  	return height - y(+d.values['percent'].toPrecision(3));
					  })
					  .attr('y', function(d){
					  	return d.values['y0'];
					  })
					  .style('fill', function(d){
					  	return colors(d.values['cluster_num']);
					  });
		}
		
		var bar_data = update_stacked_bars(cluster_sol);
		update_bar_connectors(cluster_sol, bar_data);
	}
	update_transitions_chart(5);
}