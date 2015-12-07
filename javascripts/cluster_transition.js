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

	var colors = d3.scale.category10();

	var xAxis_left = d3.svg.axis()
				  	   .scale(x_left)
	    		       .orient("bottom");

	var xAxis_middle = d3.svg.axis()
				         .scale(x_middle)
	    		         .orient("bottom");

	var yAxis = d3.svg.axis()
				  .scale(y)
				  .orient("left");

	d3.select('body')
	  .append('div')
	  .attr('class','title_container')
	  .append('h2')
	  .text('Cluster Transitions')

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

			x_left.domain(previous_cluster_sol.map(function(d) {
													return d.total;
												   }));

			//create g to hold bars
			var left_group = svg.selectAll('.left_bars')
						   .data(previous_cluster_sol, function(d) {return d.key;});

			var center_group = svg.selectAll('.center_bars')
						   .data(current_cluster_sol, function(d) {return d.key;});

			//remove bars
			var exitbars_left = left_group.exit();
			exitbars_left.remove();

			var exitbars_center = center_group.exit();
			exitbars_center.remove();

			//Enter selection
			var entergroup_left = left_group.enter()
							  				.append('g')
							  				.attr('class','left_bars')
							  				.attr('id',function(d){
							  					return d.values['cluster_num']
							  				})
							  				.attr('transform','translate('+(content_width/3-x_left.rangeBand())+',0)');

			var entergroup_center = center_group.enter()
												.append('g')
							  					.attr('class','center_bars')
							  					.attr('id',function(d){
							  						return d.values['cluster_num']
							  					})
							  					.attr('transform','translate('+(2*content_width/3+x_left.rangeBand())+',0)');

			entergroup_left.append('rect')
					  	   .attr('width', x_left.rangeBand())
					  	   .attr('class','transition_rect')
					  	   .attr('id','left_rects');

			entergroup_left.append('text')
						   .attr('class', 'segment_name left_segment_name')

			entergroup_left.append('text')
						   .attr('class', 'segment_percentage_labels segment_percentage_labels_left')

			entergroup_center.append('rect')
					  		.attr('width', x_left.rangeBand())
					  		.attr('class','transition_rect')
					  		.attr('id','center_rects');

			entergroup_center.append('text')
						   .attr('class', 'segment_name center_segment_name')

			entergroup_center.append('text')
						     .attr('class', 'segment_percentage_labels segment_percentage_labels_center')

			//update rects
			var left_group_y = {}; //This is an object for storing the y positions of each cluster for use in transition lines
			left_group.select('rect')
					  .attr('height', function(d) {
					  	return height - y(+d.values['percent'].toPrecision(3));
					  })
					  .attr('y', function(d){
					  	left_group_y[d.values['cluster_num']] =  d.values['y0']; 
					  	return d.values['y0'];
					  })
					  .style('fill', function(d){
					  	return 'black';
					  });

			var center_group_y = {}
			center_group.select('rect')
			  .attr('height', function(d) {
			  	return height - y(+d.values['percent'].toPrecision(3));
			  })
			  .attr('y', function(d){
			  	center_group_y[d.values['cluster_num']] =  d.values['y0'];
			  	return d.values['y0'];
			  })
			  .style('fill', function(d){
			  	return colors(d.values['cluster_num']);
			  });

			//Adds segment names beside stacked bars
			left_group.select('.left_segment_name')
					  .text(function(d){
					  	 return "segment " + (+d.values.cluster_num+1)
					  })
					  .attr('y', function(d){
					     return d.values['y0']+18;
					  })
					  .attr('x', '-5')

			center_group.select('.center_segment_name')
					  .text(function(d){
					  	 return "segment " + (+d.values.cluster_num+1)
					  })
					  .attr('y', function(d){
					     return d.values['y0']+18;
					  })
					  .attr('x', x_left.rangeBand()+5)

			//Adds percentage labels to segments
			left_group.select('.segment_percentage_labels')
					  .text(function(d){ 
					  	return  Math.round(d.values.percent*100,2) + "%"
					  })
					  .attr('y', function(d){
					  	return d.values['y0'] + 18;
					  })
					  .attr('x',x_left.rangeBand() )

			center_group.select('.segment_percentage_labels')
					  .text(function(d){
					  	return  Math.round(d.values.percent*100,2) + "%"
					  })
					  .attr('y', function(d){
					  	return d.values['y0'] + 18;
					  })


			svg.select('g.xAxis_left')
			   .call(xAxis_left);

			svg.select('g.yAxis')
			   .call(yAxis);

			
			//Listening for hover over stacked bars to change color on hover
			left_group.on('mouseover', function(d) {
				d3.selectAll('rect')
				  .style('fill', function(d){
			  	  return colors(d.values['cluster_num']);
			  	});
				center_group.selectAll('rect')
				  .style('fill', 'black');
				d3.selectAll('polygon.transition_poly')
				  .style('fill',function(d){
				  	return colors(d.values['from_cluster'])
				  })
			});

			center_group.on('mouseover', function(d) {
				d3.selectAll('rect')
				  .style('fill', function(d){
			  	  return colors(d.values['cluster_num']);
			  	});
				left_group.selectAll('rect')
				  .style('fill', 'black');
				d3.selectAll('polygon.transition_poly')
				  .style('fill',function(d){
				  	return colors(d.values['to_cluster'])
				})
			});

			var rects = d3.selectAll('rect')
			rects.on('mouseover', function(d) {
				var selected = d3.select(this)
				  .style('fill-opacity', 1);
				var target_rect = selected.datum().values.cluster_num;
				var location = d3.select(this).attr('id');

				if (location === 'center_rects') {
					d3.selectAll('polygon.transition_poly')
					  .style('opacity', 0)
					  .filter(function(d){
					  	return d.values.to_cluster === target_rect;
					  })
					  .style('opacity', 1);
					d3.selectAll('text.to_cluster_percent')
				  	  .filter(function(d){
				  	  	return '#to_cluster_' + d.values.to_cluster === '#to_cluster_' + target_rect
				  	  })
				  	  .style('opacity', 0.8);
				}
				if (location === 'left_rects') {
					d3.selectAll('polygon.transition_poly')
					  .style('opacity', 0)
					  .filter(function(d){
					  	return d.values.from_cluster === target_rect;
					  })
					  .style('opacity', 1);	
					d3.selectAll('text.from_cluster_percent')
				  	  .filter(function(d){
				  	  	return '#from_cluster_' + d.values.from_cluster === '#from_cluster_' + target_rect
				  	  })
				  	  .style('opacity', 0.8);
				}
			})

			rects.on('mouseout', function(d) {
				d3.select(this)
				  .style('fill-opacity', function(d){
				  	return 0.5;
				  });

				d3.selectAll('polygon.transition_poly')
				  .style('opacity', 0.2);

				d3.selectAll('text.to_cluster_percent')
				  .style('opacity', 0)

				d3.selectAll('text.from_cluster_percent')
				  .style('opacity', 0)
			})

			//What is getting returned
			var output = {'total': num_observations,
						  'previous': prev_cluster_counts,
						  'current' : current_cluster_counts,
						  'left_group_ys': left_group_y,
						  'center_group_ys': center_group_y,
						  'stacked_width': x_left.rangeBand()}

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
						   
			//remove transition lines
			var exittrans_left = left_group.exit();
			exittrans_left.remove();

			
			//Creates an array of keys for the clusters 
			var left_group_cluster_ids = Object.keys(cluster_info['left_group_ys'])
			var center_group_cluster_ids = Object.keys(cluster_info['center_group_ys'])
			//Holds the top position of each transition bar
			var transition_rectangle_left_positions = {}
			var transition_rectangle_left_to_positions = {}

			left_group_cluster_ids.forEach(function(group) {				
				transition_rectangle_left_positions[group]= cluster_info['left_group_ys'][group]
			})

			center_group_cluster_ids.forEach(function(group) {				
				transition_rectangle_left_to_positions[group]= cluster_info['center_group_ys'][group]
			})

			//Enter selection
			var trans_entergroup_left = left_group.enter()
												  .append('g')
												  .attr('class','left_transition_g')
												  .attr('transform',function(d) { 
												  	return 'translate('+cluster_info['stacked_width']+',0)';
												  })
												  .selectAll('polygon')
												  .data(function(d) {
												  	return d.values
												  })
												  .enter()
												  
			trans_entergroup_left.append('polygon')
					  	   		 .attr('class','transition_poly');

			trans_entergroup_left.append('text')
								 .attr('class', 'from_cluster_percent')

			trans_entergroup_left.append('text')
								 .attr('class', 'to_cluster_percent')
			
			//update left transitions polygons
			var left_side = (content_width/3-(+cluster_info['stacked_width']))
			var left_transition_width = (2*content_width/3)-0.5
			left_group.selectAll('polygon.transition_poly')
					  .attr('points', function(d) { //sets the 4 points of a polygon
					  	var current_y = transition_rectangle_left_positions[d.values['from_cluster']] //y position on from_clusters
					  	var transition_y = transition_rectangle_left_to_positions[d.values['to_cluster']]//y position on to_clusters
					  	var bar_height = height - y(+d.values['percent_of_total'].toPrecision(3))
					  	var top_left = left_side + "," + (current_y)
					  	var top_right = left_transition_width + "," + (transition_y)
					  	var bottom_left = left_side + "," + (current_y + bar_height)
					  	var bottom_right = left_transition_width + "," +  (transition_y + bar_height)
					  	transition_rectangle_left_positions[d.values['from_cluster']] =  current_y + bar_height
					  	transition_rectangle_left_to_positions[d.values['to_cluster']] = transition_y + bar_height
					  	return top_left + " " + top_right + " " + bottom_right + " " + bottom_left;
					  })
					  .attr('data-from', function(d){
					  	return d.values['from_cluster'];
					  })
					  .attr('data-to', function(d){
					  	return d.values['to_cluster'];
					  })
					  .style('fill', function(d){
			  			return colors(d.values['to_cluster']);
			  		  })
					  .attr('opacity', 0.2); 

			//update left transitions from percentages
			left_group.selectAll('text.from_cluster_percent')
					  .text(function(d) {
					  	return Math.round(d.values.percent_of_from_cluster*100,1) + "%"
					  })
					  .attr('id', function(d) {
					  	return "from_cluster_" + d.values.from_cluster
					  })
					  .attr('y', function(d) {
					  	var current_y = transition_rectangle_left_positions[d.values['from_cluster']] //y position on from_clusters
					  	var bar_height = height - y(+d.values['percent_of_total'].toPrecision(3))
					  	var top_left = left_side + "," + (current_y)
					  	transition_rectangle_left_positions[d.values['from_cluster']] =  current_y + bar_height
					  	return top_left
					  })
					  .attr('x',left_side)
					  .style('opacity','0')

			left_group.selectAll('text.to_cluster_percent')
					  .text(function(d) {
					  	return Math.round(d.values.percent_of_to_cluster*100,1) + "%"
					  })
					  .attr('id', function(d) {
					  	return "to_cluster_" + d.values.to_cluster
					  })
					  .attr('y', function(d) {
					  	var transition_y = transition_rectangle_left_to_positions[d.values['to_cluster']] //y position on from_clusters
					  	var bar_height = height - y(+d.values['percent_of_total'].toPrecision(3))
					  	var top_right = left_transition_width + "," + (transition_y)
					  	transition_rectangle_left_to_positions[d.values['to_cluster']] = transition_y + bar_height
					  	return top_right
					  })
					  .attr('x',left_transition_width)
					  .style('opacity','0')
		}



		var bar_data = update_stacked_bars(cluster_sol);
		update_bar_connectors(cluster_sol, bar_data);
	}
	update_transitions_chart(5);
}