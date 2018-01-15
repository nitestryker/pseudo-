<?php
// post vars 
$from = $_POST['from'];
if(empty($_POST['from'])){
print "error";
exit();
}
$to  = $_POST['to'];
$subject = $_POST['subject'];
$message = $_POST['message'];
$msgid = generateRandomString("5");
// db connection and selection
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
             or die ("Couldn't connect to server.");
            $db = mysql_select_db("$database_name", $connection)
             or die("Couldn't select database.");
$deleted = "no";
$date = new DateTime();
$date = $date->format('Y-m-d H:i:s');
$fdate = date('F j, Y  h:i:s a', strtotime($date));
$sql = mysql_query("INSERT INTO messages (msgid,to_user,from_user,deleted,subject,message,date)
      			VALUES('$msgid','$to','$from','$deleted','$subject', '$message','$fdate')") or die (mysql_error());
if (!$sql) {
        echo "There has been an error please contact the server administrator";
        exit();
        }
 echo "success";
function generateRandomString($length = 10)
    {
        $characters = "1234567890";
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[rand(0, strlen($characters) - 1)];
        }
        return $randomString;
    }
?>