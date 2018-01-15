<?php
$msgid = $_POST['msgid'];
$u = $_POST['uname'];
$m = $_POST['message'];
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
 $from = $row['from_user'];
 $to = $row['to_user'];
 $subject = $row['subject'];
 $message = $row['message']; 
}
$randomid = generateRandomString(5);
$deleted = "no";
$subject = "Re: $subject";
$sql = mysql_query("INSERT INTO messages (msgid,to_user,from_user,deleted,subject,message)
      			VALUES('$msgid','$from','$to','$deleted','$subject', '$m')") or die (mysql_error());

function generateRandomString($length = 10)
    {
        $characters = "1234567890";
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[rand(0, strlen($characters) - 1)];
        }
        return $randomString;
    }
print "your message was sent\n" 
?>