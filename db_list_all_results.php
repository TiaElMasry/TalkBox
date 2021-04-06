<?php

//------------- Retrieve Data------------------------------
            
            $sql = "SELECT ID, PHRASES FROM simplePhrases";
            $result = $mysqli->query($sql);
            
            echo "<h2>Talk to People Phrases listed</h2>";
            if ($result->num_rows > 0) {
              
              // output data of each row
              
              //----start table------------------
              
              echo '<table style="width:100%">';
              
            // echo "<tr>";
             // echo "<th>Phrase ID</th>";
              //echo "<th>Phrase</th>";
              
              echo "</tr>";
              
              while($row = $result->fetch_assoc()) {
                
                echo "<tr>";
                //echo "<td>".$row["ID"]."</td><td>".$row["PHRASES"]."</td></tr>";
                echo "<td>".$row["PHRASES"]."</td></tr>";
              }
              
              echo '</table>';
              
            } else {
              echo "0 results";
            }
            
            Echo "<hr>";
            
            $sql2 = "SELECT ID, Phrase FROM homeDevices";
            $result2 = $mysqli->query($sql2);
            
            echo "<h2>Talk to Devices Phrases listed</h2>";
            if ($result2->num_rows > 0) {
              
              // output data of each row
              
              //----start table------------------
              
              echo '<table style="width:100%">';
              
              
              echo "</tr>";
              
              while($row = $result2->fetch_assoc()) {
                
                echo "<tr>";
                echo "<td>".$row["Phrase"]."</td></tr>";
              }
              
              echo '</table>';
              
            } else {
              echo "0 results";
            }
            
?>
