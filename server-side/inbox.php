<?php
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
     or die ("Couldn't connect to server.");
   	    $db = mysql_select_db("$database_name", $connection)
               or die("Couldn't select database.");
$user = $_POST['user'];
$query = mysql_query("SELECT * FROM messages WHERE to_user = '$user' AND deleted = 'no' ORDER BY msgid")or die(mysql_error());
while($row = mysql_fetch_array($query))
{ 
 $message_id = $row['msgid'];
 $from = $row['from_user'];
 $subject = $row['subject'];
 print "\n";
 print "$message_id  $from - $subject\n";

}
if ($message_id == ""){
print "no messages";
}
?>