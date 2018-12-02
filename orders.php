<?php
        header('Content-type: text/html; charset:utf8');
        include('inc/header.inc.php');
        include('inc/connect.inc.php');
	$timer = 60;
	$arb1 = rand(653, 901);
	$arb2 = rand(401, 600);
#	$js_arbitrage = exec('node /var/www/html/trading/js/main.js');
#
?>

<div id="menu">
        <ul>
                <li><a href="index.php" >EXCHANGES</a></li>
                <li><a href="orders.php" style="background-color:#d6d6c2">ORDERS</a></li>

        </ul>
</div>


<?php	
	if (isset($_POST['json_refresh'])){
		$sql_select_10_query = "SELECT * FROM arbitrage";
		$last_10_arbitrage_data = mysql_query($sql_select_10_query, $con);
	}
	
        if (isset($_POST['close_action'])){
                $output = exec('python /var/www/html/trading/deploy.py');
                echo "<span style='text-align:center'><p style='font-size:18px'><b><font color='green'><b>PERFECT : </font> Action 'close' has been submitted!</b></p></span><br/><br/>";

        }

        if (isset($_POST['update_pair_amount'])) {
                if (empty($_POST['pair'])) {
                        echo "<span style='text-align:center'><p style='font-size:18px'><b><font color='red'><b>WARNING : </font> Pair field is empty.</b></p></span><br/><br/>";
                }
                elseif (empty($_POST['amount'])) {
                        echo "<span style='text-align:center'><p style='font-size:18px'><b><font color='red'><b>WARNING : </font> Amount field is empty.</b></p></span><br/><br/>";
                }
                else {  
                        $update_pair_amount_Query="UPDATE actions SET 
                                                pair = '$_POST[pair]', amount  = '$_POST[amount]'  WHERE id = '$_POST[id]'";
                        mysql_query($update_pair_amount_Query, $con);
                        echo "<span style='text-align:center'><p style='font-size:18px'><font color='green'><b>PERFECT : </font> New value's been submitted!</b></p></span><br/><br/>";
                       # $js_arbitrage = exec("python -c 'import deploy; print deploy.beta()'");        
		#	$js_arbitrage = exec('python /var/www/html/trading/py/lef/arbitrage.py');
                }
	}
	if (isset($_POST['find_arbitrage'])) {
		$py_arbitrage = exec('python /var/www/html/trading/py/lef/arbitrage.py');
        }


        echo
                "<table width='80%' >
			<meta http-equiv='refresh' content='";echo $timer; echo"' > 
                        <tr style='background-color:#FFFFF0'>
                                <th>PAIR & AMOUNT</th>
                                <th>CLOSE</th>
                        </tr>";
                        $sql_select_actions_query="SELECT * FROM actions";
                        $store_sql_select_actions = mysql_query($sql_select_actions_query, $con);
                        while ($record = mysql_fetch_array($store_sql_select_actions)){
		                echo
		                        "<form action='' method='POST'>
		                                <tr style='border-style:none'>
		                                        <td style='border-style:none'>
		                                                <input type='text' name='pair' value='$record[pair]'/><input type='hidden' name='id' value='$record[id]'/>
		                                                <input type='text' name='amount' value='$record[amount]'/>
		                                                <input type='submit' name='update_pair_amount' value='SUBMIT'/>
		                                        </td>
		                                        <td style='border-style:none'>
		                                                <input type='submit' name='close_action' value='SUBMIT'/>
		                                        </td>
		                                </tr>";
                        }
        echo "</table>";	
        echo "<table width='100%'><br>
        <tr style='background-color:#FFFFF0'>
                <th>ARBITRAGE :</th>
        </tr>";
	echo "<table width='100%'>
	<tr style='background-color:#FFFFFF'>
		
	</tr>";
		echo "<form action='orders.php' method='POST'>
		<tr style='border-style:none'>
			<td style='border-style:none'>
				<input type='text' id='arbitrage' name='arbitrage' value='$py_arbitrage' />
				<input type='submit' name='find_arbitrage' value='SUBMIT'/>
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
                                <div name='account'>HITBTC : $record2[hitbtc]</div>
                                <div name='account'>TOTAL : $record2[total]</div>
                                <div name='account'>TIMESTAMP : $record2[import_date]</div>
                                <input type='submit' name='account_refresh' value='REFRESH'/> <!-- THIS IS FOR PYTHON CALL -->

                        </td>

                </tr>";
        }
        echo "</table>";
	
		$record3 = mysql_fetch_array($last_10_arbitrage_data);
                      
	echo"<br><form id='form1' method='post' action='orders.php' style='text-align:center'>
		        <fieldset>
		                <legend style= 'margin-left:40%'>JSON Return: </legend>";
				while ($record3 = mysql_fetch_array($last_10_arbitrage_data)){

		                	echo"<div style='text-align:center'> $record3[pair] - $record[arbitrage]</div>";
					echo"<div>$record3[arbitrage]</div>";
			}
		        echo"</fieldset>
			<input type='submit' style='margin-left:46.7%' name='json_refresh' value='REFRESH'/>
		</form>";


		
?>

<br><br><br><br>
</div>
<br><br>

<?php
        include('inc/footer.inc.php');
?>

