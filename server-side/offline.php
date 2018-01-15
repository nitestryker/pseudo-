<?php

$uid = $_POST['uid'];
error_reporting(E_ALL);
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
     or die ("Couldn't connect to server.");
   	    $db = mysql_select_db("$database_name", $connection)
               or die("Couldn't select database.");
$online = 0;
$sql = "UPDATE puser SET online='$online' WHERE uid ='$uid'";
$result = mysql_query($sql);
while ($row = mysql_fetch_array($result)) {
$username = $row['identity'];
}
?>