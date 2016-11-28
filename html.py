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
	      <a class="navbar-brand" href={} >CSCI 5722 Project</a>
	    </div>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href={} >Home</a></li>
	    </ul>
	  </div>
	</nav>

	<div class="container">
		<div class="jumbotron">
			<h1>CSCI 5722 Project</h1>      
			<p>Results</p>
		</div>
		<div>
            		<h1>Cluster Results for <a href={}>{}</a></h1>
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
	      <a class="navbar-brand" href={} >CSCI 5722 Project</a>
	    </div>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href={} >Home</a></li>
	    </ul>
	  </div>
	</nav>
	<div class="container">
		<div class="jumbotron">
			<h1>CSCI 5722 Project</h1>      
			<p>Welcome! Click the drop down below to see what clusters have been found.</p>
		</div>
		<div class="dropdown">
		    <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Clusters
		    <span class="caret"></span></button>
		    <ul class="dropdown-menu">
			{}
		    </ul>
		</div>
	</div>
    </body>
</html> """
