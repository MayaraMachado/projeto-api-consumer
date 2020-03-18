<?php
	switch ($_SERVER["SCRIPT_NAME"]) {
		case "/projeto-api-consumer/php-proj/about.php":
			$CURRENT_PAGE = "About"; 
			$PAGE_TITLE = "Sobre";
			break;
		case "/projeto-api-consumer/php-proj/contact.php":
			$CURRENT_PAGE = "Contact"; 
			$PAGE_TITLE = "Contato";
			break;
		default:
			$CURRENT_PAGE = "Index";
			$PAGE_TITLE = "Home!";
	}
?>