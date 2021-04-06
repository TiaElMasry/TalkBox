<?php

include "db_connect.php";
date_default_timezone_set('America/Toronto');  

$phrase = $_GET["phrase"];
$category=$_GET["category"];

echo "<h2>Adding Phrase. Please wait. </h2>";
echo "<h2>Phrase is:</h2>";
echo "<h4>$phrase</h4>";
echo "<h4>Phrase is added to: </h4>";
echo "<h4>$category</h4>";

if ($category == "TalkToPeople"){
    $sql = "INSERT INTO simplePhrases (ID, PHRASES) VALUES (NULL,'$phrase')";
}
if($category == "TalkToDevices"){
    $sql = "INSERT INTO homeDevices (ID, Phrase) VALUES (NULL,'$phrase')";
}
if ($result = $mysqli->query($sql) === TRUE){
    echo "New record created successfully";
} else{
    echo "Error: ".$sql."<br>".$mysqli->error;
}




?>
<br><a href="index.php">Return to main page</a>
