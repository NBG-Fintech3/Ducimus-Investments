x`﻿<?php
	header('Content-type: text/html; charset:utf8');
	include('inc/header.inc.php');
	include('inc/connect.inc.php');	
?>

<div id="menu">
	<ul>
		<li><a href="index.php" >EXCHANGES</a></li>
		<li><a href="orders.php" style="background-color:#d6d6c2">ORDERS</a></li>
	
	</ul>
</div>


<?php
	# We want the close or open amount with the greatest id as it is the last inserted!
	#$sql_min_open_amount="SELECT * FROM actions WHERE action = 'open' ORDER BY id DESC LIMIT 1";
	#$data = mysql_query($sql_min_open_amount, $con);
	#$data_minimum_open_amount = mysql_fetch_array($data);
	if (isset($_POST['update1'])) {
		if ( empty($_POST['pair'])) {
			echo "<span style='text-align:center'><p style='font-size:18px'><b><font color='red'><b>WARNING : </font> Pair field is empty dude.</b></p></span><br/><br/>";
		}
		else {
			$updateQuery="UPDATE pairs
						  SET pair = '$_POST[pair]'
						  WHERE pair = '$_POST[update_value]'";
			mysql_query($updateQuery, $con);
			$updateQuery2="UPDATE actions
						  SET amount = '$_POST[amount]'
						  WHERE amount = '$_POST[open_amount]'";
			mysql_query($updateQuery2, $con);
			echo "<span style='text-align:center'><p style='font-size:18px'><font color='green'><b>PERFECT : </font> New 'PAIR' value's been submitted!</b></p></span><br/><br/>";
		}
	}
	if (isset($_POST['open_action'])) {

			$updateQuery="UPDATE actions
						  SET amount = '$_POST[amount]'
						  WHERE amount = '$_POST[open_amount]'";
			mysql_query($updateQuery, $con);
			echo "<span style='text-align:center'><p style='font-size:18px'><font color='green'><b>PERFECT: </font>New 'OPEN' amount!</b></p></span><br/><br/>";
		
	}
	#if (isset($_POST['close_action'])) {
	#	if ( empty($_POST['close'])) {
	#		echo "<span style='text-align:center'><p style='font-size:18px'><b><font color='red'><b>WARNING: </font>Amount field is empty dude.</b></p></span><br/><br/>";
	#	}
	#	else {
	#		$insertQuery="INSERT INTO actions (action, amount )		
	#				VALUES ('close','$_POST[close]')";
	#		mysql_query($insertQuery, $con);
	#		echo "<span style='text-align:center'><p style='font-size:18px'><font color='green'><b>PERFECT: </font>New 'CLOSE' amount!</b></p></span><br/><br/>";
	#	}
	#}


	$sql1="SELECT * FROM actions";
	$mydata1 = mysql_query($sql1, $con);
	echo "<table width='80%' >
	<tr style='background-color:#FFFFF0'>
		<th>PAIR & AMOUNT</th>
		
		<th>CLOSE</th>
	</tr>";
	while ($record1 = mysql_fetch_array($mydata1)){
		echo "<form action='orders.php' method='POST'>
		<tr style='border-style:none'>
			<td style='border-style:none'>
				<input type='text' name='pair' value='$record1[pair]'/><input type='hidden' name='update_value' value='$record1[pair]'/><input type='text' name='amount' value='$record1[amount]' /><input type='hidden' name='open_amount' value='$record1[amount]'/><input type='submit' name='update1' value='SUBMIT'/>
			</td>
			<td style='border-style:none'>
				<input type='submit' name='close_action' value='SUBMIT'/>
			</td>
		</tr>";
	}
	echo "</table>";

	#$sql_open_amount = "SELECT amount FROM actions";
	#$mydata2 = mysql_query($sql_open_amount, $con);
	#echo "<table width='100%'><br>
	#<tr style='background-color:#FFFFF0'>
	#	<th>OPEN AMOUNT</th>
	#</tr>";
	#while ($record5 = mysql_fetch_array($mydata2)){
	#	echo "<form action='orders.php' method='POST'>
	#	<tr style='border-style:none'>
	#		<td style='border-style:none'>
	#			<input type='text' name='amount' value='$record5[amount]' /><input type='hidden' name='open_amount' value='$record5[amount]'/><input type='submit' name='open_action' value='SUBMIT'/>
	#		</td>
	#	</tr>";
	#}
	echo "</table>";

	echo "<table width='100%'><br>
	<tr style='background-color:#FFFFF0'>
		<th>ARBITRAGE</th>
	</tr>";
		echo "<form action='orders.php' method='POST'>
		<tr style='border-style:none'>
			<td style='border-style:none'>
				<input type='text' name='amount' value='5.3254' /><input type='submit' name=' ' value='REFRESH'/>
			</td>
		</tr>";
	
	echo "</table>";


	$sql_account_data = "SELECT * FROM account_info";
	$account_data = mysql_query($sql_account_data, $con);
	echo "<table width='100%' display: inline-block' ><br><br>
	<tr style='background-color:#FFFFF0'>
		<th>ACCOUNT INFO</th>
	</tr>";
	while ($record2 = mysql_fetch_array($account_data)){
		echo "<form action='orders.php' method='POST'>
		<tr style='border-style:none; background-color:#ccffcc'>
			<td >
				<div name='account'>OKEX : $record2[okex]</div>
				<div name='account'>HITBTC : $record2[okex]</div>
				<div name='account'>TOTAL : $record2[total]</div>
				<div name='account'>TIMESTAMP : $record2[import_date]</div>
				<input type='submit' name='close_action' value='REFRESH'/> <!-- THIS IS FOR PYTHON CALL -->

			</td>

		</tr>";
	}
	echo "</table>";





echo"
<br><br>
<form id='form1' method='post' action='orders.php'>
<fieldset>
	<legend style= 'text-align:center'> JSON RETURN: </legend>

</fieldset>
</form>";

?>
<br><br><br><br>
</div>





<br><br>

<?php
	include('inc/footer.inc.php');
?>
