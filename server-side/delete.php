<?php
$msgid = $_POST['msgid'];
$uid = $_POST['uid'];
// update online status 
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
             or die ("Couldn't connect to server.");
            $db = mysql_select_db("$database_name", $connection)
             or die("Couldn't select database.");
$query = mysql_query("SELECT * FROM messages WHERE msgid = '$msgid'")or die(mysql_error());
while($row = mysql_fetch_array($query))
{ 
 $message_id = $row['msgid'];
 $to_user  = $row['to_user'];
 $from = $row['from_user'];
 $subject = $row['subject'];
}

$delete = "yes";
 mysql_query("UPDATE messages SET deleted='$delete' WHERE msgid ='$msgid'");
print "message #$msgid has been deleted";
?>