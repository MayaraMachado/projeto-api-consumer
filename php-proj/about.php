<?php include("includes/a_config.php");?>
<!DOCTYPE html>
<html>
<head>
	<?php include("includes/head-tag-contents.php");?>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

</head>
<body>
<?php include("includes/design-top.php");?>
<?php include("includes/navigation.php");?>
<!-- Set up a container element for the button -->

<!-- Include the PayPal JavaScript SDK -->
<script src="https://www.paypal.com/sdk/js?client-id=sb&currency=USD"></script>

<script>

	const queryString = window.location.search;
	console.log(queryString);
	const urlParams = new URLSearchParams(queryString);
	const filme = urlParams.get('filme')

	fetch('http://127.17.0.1:443/api/v2/filme/'+filme)
            .then((res) => res.json())
            .then((data) => {
	    console.log(data.filmes)
		 document.getElementById("titulo").innerHTML = data['nome'];
		 document.getElementById("sinopse").innerHTML = data['sinopse'];
		 document.getElementById("poster").src = data['poster'];
	     console.log(data);
            });

	// Render the PayPal button into #paypal-button-container
	paypal.Buttons({

		// Set up the transaction
		createOrder: function(data, actions) {
			return actions.order.create({
				purchase_units: [{
					amount: {
						value: '0.01'
					}
				}]
			});
		},

		// Finalize the transaction
		onApprove: function(data, actions) {
			return actions.order.capture().then(function(details) {
				// Show a success message to the buyer
				alert('Transaction completed by ' + details.payer.name.given_name + '!');
			});
		}


	}).render('#paypal-button-container');
</script>

<div class="container" id="main-content">
	<div class="media">
		<img id="poster" src=".." class="mr-3" alt="...">
		<div class="media-body">
			<h5 id="titulo" class="mt-0">Titulo do flme</h5>
			<p id="sinopse">Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
			<div id="paypal-button-container"></div>
		</div>
	</div>

	</div>
</div>

<?php include("includes/footer.php");?>

</body>
</html>
