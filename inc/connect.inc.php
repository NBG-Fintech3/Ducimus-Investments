<?php
	header('Content-type: text/html; charset: utf8');
	$con = mysql_connect("127.0.0.1","root","iwant1000000$");
	mysql_query("SET NAMES 'utf8'", $con);
	if (!$con){
		die("Could not connect: " . mysql_error());
	}
	mysql_select_db("trading_db",$con);
?>
