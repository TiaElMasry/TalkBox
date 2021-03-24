<?php

include "db_connect.php";
date_default_timezone_set('America/Toronto');  

$phrase = $_GET["phrase"];


echo "<h2>Adding Phrase. Please wait. </h2>";
echo "<h2>Phrase is:</h2>";
echo "<h4>$phrase</h4>";

$sql = "INSERT INTO simplePhrases (ID, PHRASES) VALUES (NULL,'$phrase')";

if ($result = $mysqli->query($sql) === TRUE){
    echo "New record created successfully";
} else{
    echo "Error: ".$sql."<br>".$mysqli->error;
}




?>
<br><a href="index.php">Return to main page</a>