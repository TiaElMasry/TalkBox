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
            <label for="l"> Phrase:</label>
            <input type="text" id="phrase" name="phrase" value="enter a phrase">
            <select name="category" id="category">
            <option value="0" selected="selected">Select the phrase category</option>
            <option value="TalkToPeople">Talk to People</option>
            <option value="TalkToDevices">Talk to Devices</option>
            </select>
            <input type="submit" value="Submit">  
            
            
            
        </form>
        <hr>
        
        
        
        
         
      <?php   
         
         include "db_list_all_results.php";
         
            $mysqli->close();
           
        ?>
        
    </body>
    
</html>
