<?php 
error_reporting(E_ALL);
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
     or die ("Couldn't connect to server.");
   	    $db = mysql_select_db("$database_name", $connection)
               or die("Couldn't select database.");
$sql = "SELECT * FROM  puser WHERE online = '1'";
$result = mysql_query($sql);
while ($row = mysql_fetch_array($result)) {
$username = $row['identity'];
print "  $username\n";
}
?>