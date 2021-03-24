<?php

//------------- Retrieve Data------------------------------
            
            $sql = "SELECT ID, PHRASES FROM simplePhrases";
            $result = $mysqli->query($sql);
            
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
                echo "<td>".$row["ID"]."</td><td>".$row["PHRASES"]."</td></tr>";
              }
              
              echo '</table>';
              
            } else {
              echo "0 results";
            }
            
?>