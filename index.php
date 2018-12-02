<?php
	header('Content-type: text/html; charset:utf8');
	include('inc/header.inc.php');
	include('inc/connect.inc.php');	
?>

<div id="menu">
	<ul>
		<li><a href="index.php" style="background-color:#d6d6c2">EXCHANGES</a></li>
		<li><a href="orders.php">ORDERS</a></li>
	
	</ul>
</div>


<?php
if (isset($_POST['addnew'])) {
	if ( (empty($_POST['okex_api_key'])) and empty($_POST['okex_secret_key']) and empty($_POST['okex_passphrase']) and empty($_POST['hitbtc_api_key']) and empty($_POST['hitbtc_secret_key']) and empty($_POST['hitbtc_passphrase']))	 {
		echo "<span style='text-align:center'><p style='font-size:18px'><font color='red'><b>WARNING: </font> You need to fill in something dude! Please try again.</b></p></span><br/><br/>";
	}
	else {
		$addQuery="INSERT INTO exchange_credentials (exchange, api_key, secret_key, passphrase)		
					VALUES ('okex','$_POST[okex_api_key]','$_POST[okex_secret_key]','$_POST[okex_passphrase]')";
		$addQuery2="INSERT INTO exchange_credentials (exchange, api_key, secret_key, passphrase)		
					VALUES ('hitbtc','$_POST[hitbtc_api_key]','$_POST[hitbtc_secret_key]','$_POST[hitbtc_passphrase]')";			
		mysql_query($addQuery,$con); 
		mysql_query($addQuery2,$con); 
		#echo "<span style='text-align:center'><p style='font-size:18px'><font color='green'><b>PERFECT: </font> Your data's been successfully stored!</b></p></span><br/><br/>";
	}
}

echo"
<form id='form1' method='post' action='index.php'>
<fieldset>
	<legend>Store data from exchanges in MySQL DB :</legend>
	<p style='text-align:center; margin-right:5%'>OKEX EXCHANGE : </p>
	<label for='okex_api_key'>
		<span>API - KEY :</span>
		<input id='okex_api_key' type='text' name='okex_api_key' size='40'/>
	</label>
	<label for='okex_secret_key'>
		<span>SECRET - KEY:</span>
		<input id='okex_secret_key' type='text' name='okex_secret_key' size='40'/>
	</label>
	<label for='okex_passphrase'>
		<span>PASSPHRASE :</span>
		<input id='okex_passphrase' type='text' name='okex_passphrase' size='40'/>
	</label>
<br><br>
	<p style='text-align:center; margin-right:5%'>HITBTC EXCHANGE : </p>
	<label for='hitbtc_api_key'>
		<span>API - KEY :</span>
		<input id='hitbtc_api_key' type='text' name='hitbtc_api_key' size='40'/>
	</label>

	<label for='hitbtc_secret_key'>
		<span>SECRET - KEY :</span>
		<input id='number' type='text' name='hitbtc_secret_key' size='40'/>
	</label>
	<label for='hitbtc_passphrase'>
		<span>PASSPHRASE :</span>
		<input id='hitbtc_passphrase' type='text' name='hitbtc_passphrase' size='24'/>
	</label>


	<label for='submit1' id='submit'>
		<input id='submit1' class='submit' type='submit' name='addnew' value='Submit'/>
	</label>

</fieldset> 
</form>";

?>
<br><br>

<?php
	include('inc/footer.inc.php');
?>
