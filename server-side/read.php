<?php
$msgid = $_POST['msgid'];
$uid = $_POST['uid'];
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
 $msgid = $row['msgid'];
 $to = $row['to_user'];
 $date = $row['date'];
 $from = $row['from_user'];
 $subject = $row['subject'];
 $message = $row['message']; 
 // prevent people from reading other peoples mail
 if ($to != $uid){
 exit(); 
// not authorized owner"
print  "nao";
}
 print "\n";
 print "Date: $date \n";
 print "\n";
 print  "To: $to \n";
 print "\n";
 print "From: $from \n";
 print "\n";
 print "Subject: $subject\n";
 print "\n";
 print "\n";
 print " $message\n";
 print "---------------------------------\n";
}
if ($msgid == ""){
print "no message \n";
}
?>