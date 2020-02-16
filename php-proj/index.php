<?php include("includes/a_config.php");?>
<!DOCTYPE html>
<html>
<head>
	<?php include("includes/head-tag-contents.php");?>
</head>
<body>

<?php include("includes/design-top.php");?>
<?php include("includes/navigation.php");?>


<script type="text/javascript">

            fetch('http://0.0.0.0:5000/api/v1/filmes/emcartaz')
            .then((res) => res.json())
            .then((data) => {
            var j = JSON.stringify(data);
            var arrayLength = data['filmes'].length;
            var innerHtml = "<div style='align-text: center;margin-left: 60px;' class='row center-block'>";
	    for (var i = 0; i < arrayLength; i++) {
		var film = data['filmes'][i];
		console.log(film);
		innerHtml += "<div class='card' style='width: 18rem;margin: 15px;'>"
			    +"<img src= '"+film['poster']+ "' class='card-img-top' alt='...'>"
			    + "<div class='card-body'>"
			    + "<h5 class='card-title'>"+film['nome']+"</h5>"
			    + "<p class='card-title' style='color:blue;font-size=11px;'>"+film['data']+"</p>"
			    + "<p class='card-text'>"+film['sinopse']+"</p>"
			    + "<a href='#' class='btn btn-primary'>Leia mais + </a>"
			    + "</div></div>";
	     }
	     innerHtml += "</div>";
	     document.getElementById("movies-list").innerHTML = innerHtml;
	     console.log(data);
            });
</script>

<div class="container" id="main-content">

	<h2>Filmes em cartaz!</h2>

	<div id="movies-list"></div>

</div>
<?php include("includes/footer.php");?>

</body>
</html>
