<?php

// Variables connect to database
        $host = "localhost";
        $username = "zbadawi99";
        $password = "talkBox";
        $database = "talkBox";
        
         //Create a DB connect
        
            $mysqli = new mysqli($host, $username, $password, $database);
            
            if ($mysqli->connect_errno) {
                    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
                }
            echo $mysqli->host_info . "<br>";

?>