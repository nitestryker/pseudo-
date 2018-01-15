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
$sql = "SELECT * FROM  puser WHERE uid = uid ORDER BY identity";
$result = mysql_query($sql);
while ($row = mysql_fetch_array($result)) {
$username = $row['identity'];
$status = $row['online'];
switch ($status) {
 case "0":
 $status = "offline";
 break;
 case "1":
 $status = "online";
break;
}
print "  $username \n";
}
?>