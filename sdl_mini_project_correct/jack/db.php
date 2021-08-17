<?php

$servername = "localhost";
$dBUsername = "root";
$dbPassword = "";
$dBName = "database";

$con = mysqli_connect($servername, $dBUsername, $dbPassword, $dBName);

if(!$con){
	echo "Databese Connection Failed";
}

?>