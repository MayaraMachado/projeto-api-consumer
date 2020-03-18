<?php include("includes/a_config.php");?>
<!DOCTYPE html>
<html>
<head>
	<?php include("includes/head-tag-contents.php");?>
	<meta charset="utf-8">
</head>
<body>
<?php include("includes/design-top.php");?>


<script type="text/javascript">

            fetch('http://127.17.0.1:443/api/v2/filmes')
            .then((res) => res.json())
            .then((data) => {
	    console.log(data.filmes)
            var j = JSON.stringify(data.filmes);
            var arrayLength = data.filmes.length;
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
			    + "<a href='about.php?filme="+film['id']+ "' class='btn btn-primary'>Comprar </a>"
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
