formatString = """
<!DOCTYPE html>
<html>
    <head>
        <title>Cluster Results</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>

    <body>
	<nav class="navbar navbar-default">
	  <div class="container-fluid">
	    <div class="navbar-header">
	      <a class="navbar-brand" href= "/" >CSCI 5722 Project</a>
	    </div>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href= "/" >Home</a></li>
	    </ul>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href= "/cluster_page/" >Cluster Selection</a></li>
	    </ul>
	  </div>
	</nav>

	<div class="container">
		<div class="jumbotron">
			<h1>CSCI 5722 Project</h1>      
			<p>Results</p>
		</div>
		<div>
			<h1>Cluster Results for <a href=\"{}\">{}</a><img src={} style=\"height:200px;width:200px;image-orientation: from-image;\"></h1>
		   	<ul>
		       		{}
		    	</ul>
        	</div>
	</div>

   </body>
</html>"""

indexString = """
<!DOCTYPE html>
<html>
    <head>
        <title>Cluster Results</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>

    <body>
	<nav class="navbar navbar-default">
	  <div class="container-fluid">
	    <div class="navbar-header">
	      <a class="navbar-brand" href= "/" >CSCI 5722 Project</a>
	    </div>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href= "/" >Home</a></li>
	    </ul>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href= "/cluster_page/" >Cluster Selection</a></li>
	    </ul>
	  </div>
	</nav>
	<div class="container">
		<div class="jumbotron">
			<h1>CSCI 5722 Project</h1>      
			<p>Click the drop down below to see what clusters have been found.</p>
		</div>
		<form action="/detail_page/" method="post">
			<div class="form-group">
	      			<label for="cluster">Cluster:</label>
	      			<select class="form-control" name="cluster" id="cluster">
					{}
				</select>
			</div>
		 	<button type="submit" class="btn btn-primary">View Cluster Results</button>
		</form>
	</div>
    </body>
</html> """

peopleString = """
<!DOCTYPE html>
<html>
    <head>
        <title>Cluster Results</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>

    <body>
	<nav class="navbar navbar-default">
	  <div class="container-fluid">
	    <div class="navbar-header">
	      <a class="navbar-brand" href= "/" >CSCI 5722 Project</a>
	    </div>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href= "/" >Home</a></li>
	    </ul>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href= "/cluster_page/" >Cluster Selection</a></li>
	    </ul>
	  </div>
	</nav>
        <ul>
            {}
        </ul>
    </body>
</html>"""
