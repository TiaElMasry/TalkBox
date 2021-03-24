<html>
    <head>
         <?php
        
        include "db_connect.php";
      
   ?>   
      
    </script>
        
    </head>
    
    <body>
        <h1>
            Phrases Entry Page   
        </h1>
        
       
   
   <div id="map"></div>
   
    <hr>
        <h2>Enter Phrase Information</h2>
        
         <form action="db_insert.php">
             <!--------------- LAT--------------------->
            <label for="l"> Simple Phrase:</label>
            <input type="text" id="phrase" name="phrase" value="enter a phrase">
            <input type="submit" value="Submit">
            
            
        </form>
        <hr>
        
        
        
        
         
      <?php   
         echo "<h2>All Phrases listed</h2>";
         
         include "db_list_all_results.php";
         
            $mysqli->close();
           
        ?>
        
    </body>
    
</html>