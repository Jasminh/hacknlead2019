<%@ page contentType="text/html; charset = UTF-8"%>
<%@taglib uri="http://www.springframework.org/tags/form" prefix="form"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html lang="en">
<head>
<title>Bootstrap 4 Website Example</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet"
	href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script
	src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script
	src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
<link
	href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css"
	rel="stylesheet" />
<script
	src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js"></script>
<link rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/chosen/1.5.1/chosen.min.css">
<script
	src="https://cdnjs.cloudflare.com/ajax/libs/chosen/1.5.1/chosen.jquery.min.js"></script>
<script src="https://d3js.org/d3.v4.js"></script>
<script src="https://d3js.org/d3-scale-chromatic.v1.min.js"></script>
	
	
	
<style>
.fakeimg {
	height: 200px;
	background: #aaa;
}

.dropdown {
	margin: 20px;
}

.dropdown-menu {
	max-height: 20rem;
	overflow-y: auto;
}

.btn-xl {
	padding: 10px 70px;
	font-size: 20px;
	border-radius: 10px;
}

.txtHeader {
	font-size: 20px;
	padding: 30px;
}
</style>




</head>
<body>

	<div class="jumbotron text-center" style="margin-bottom: 0;background-image: url('../../img/background.jpg'); ">
		<img border="0" src="img/background.jpg" alt="Pulpit rock" width="304" height="228">
		<h1>The Good Explorers</h1>
		<p>Fighting Modern Slavery through Technology</p>
	</div>

	<nav class="navbar navbar-expand-sm bg-dark navbar-dark"></nav>

	<%-- <div style="width: 520px; margin: 0px auto; margin-top: 30px;">
		<h2>Select Product :</h2>
		<select class="chosen" style="width: 500px;">
			<c:forEach items="${productlist}" var="category">
				<option value="${category.productName}" href="#section1">${category.productName}</option>
			</c:forEach>
		</select>
	</div> --%>


	<div class="container" style="margin-top: 30px">
		<div class="row">
			<div class="col-sm-4">
				<h3>What are you interested at </h3>
			</div>
			<div class="col-sm-4">
				<select class="chosen" style="width: 500px;" placeholder="Search">
					<c:forEach items="${dataList}" var="category">
						<option value="${category.productName}">${category.productName}</option>
					</c:forEach>
				</select>
			</div>
		</div>
	</div>

	<div class="container" style="margin-top: 30px">
		<div class="row">
			<div class="col-sm-4">
				<h3>And where</h3>
			</div>
			<div class="col-sm-4">
				<select class="chosen" style="width: 500px;">
					<c:forEach items="${dataList}" var="category">
						<option>Search</option>
						<option value="${category.country}">${category.country}</option>
					</c:forEach>
				</select>
			</div>
		</div>
	</div>

	<!-- Create a div where the graph will take place -->
	<div id="my_dataviz" style="margin-left:100px"></div>


	<!-- <div class="jumbotron text-center" style="margin-bottom: 0">
		<p>Footer</p>
	</div> -->

	<script>
		$(".chosen").chosen();

		function myFunction() {
			alert(document.getElementById("dropdown_coins").value);
		}
		
		// set the dimensions and margins of the graph
		var width = 1000
		    height = 1000
		    margin = 300

		// The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
		var radius = Math.min(width, height) / 2 - margin

		// append the svg object to the div called 'my_dataviz'
		var svg = d3.select("#my_dataviz")
		  .append("svg")
		    .attr("width", width)
		    .attr("height", height)
		  .append("g")
		    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

		// Create dummy data
		var data = {prevalence_score: 9, vulnerability_score: 20, support_survivors_percentage:30, address_risk_percentage:8, neg_government_complicity:12, criminal_justice_percentage:3, support_survivors:7, address_risk_percentage:14}

		// set the color scale
		var color = d3.scaleOrdinal()
		  .domain(["a", "b", "c", "d", "e", "f", "g", "h"])
		  .range(d3.schemeDark2);

		// Compute the position of each group on the pie:
		var pie = d3.pie()
		  .sort(null) // Do not sort group by size
		  .value(function(d) {return d.value; })
		var data_ready = pie(d3.entries(data))

		// The arc generator
		var arc = d3.arc()
		  .innerRadius(radius * 0.5)         // This is the size of the donut hole
		  .outerRadius(radius * 0.8)

		// Another arc that won't be drawn. Just for labels positioning
		var outerArc = d3.arc()
		  .innerRadius(radius * 0.9)
		  .outerRadius(radius * 0.9)

		// Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
		svg
		  .selectAll('allSlices')
		  .data(data_ready)
		  .enter()
		  .append('path')
		  .attr('d', arc)
		  .attr('fill', function(d){ return(color(d.data.key)) })
		  .attr("stroke", "white")
		  .style("stroke-width", "2px")
		  .style("opacity", 0.7)

		// Add the polylines between chart and labels:
		svg
		  .selectAll('allPolylines')
		  .data(data_ready)
		  .enter()
		  .append('polyline')
		    .attr("stroke", "black")
		    .style("fill", "none")
		    .attr("stroke-width", 1)
		    .attr('points', function(d) {
		      var posA = arc.centroid(d) // line insertion in the slice
		      var posB = outerArc.centroid(d) // line break: we use the other arc generator that has been built only for that
		      var posC = outerArc.centroid(d); // Label position = almost the same as posB
		      var midangle = d.startAngle + (d.endAngle - d.startAngle) / 2 // we need the angle to see if the X position will be at the extreme right or extreme left
		      posC[0] = radius * 0.95 * (midangle < Math.PI ? 1 : -1); // multiply by 1 or -1 to put it on the right or on the left
		      return [posA, posB, posC]
		    })

		// Add the polylines between chart and labels:
		svg
		  .selectAll('allLabels')
		  .data(data_ready)
		  .enter()
		  .append('text')
		    .text( function(d) { console.log(d.data.key) ; return d.data.key } )
		    .attr('transform', function(d) {
		        var pos = outerArc.centroid(d);
		        var midangle = d.startAngle + (d.endAngle - d.startAngle) / 2
		        pos[0] = radius * 0.99 * (midangle < Math.PI ? 1 : -1);
		        return 'translate(' + pos + ')';
		    })
		    .style('text-anchor', function(d) {
		        var midangle = d.startAngle + (d.endAngle - d.startAngle) / 2
		        return (midangle < Math.PI ? 'start' : 'end')
		    })
	</script>
</body>

</html>
