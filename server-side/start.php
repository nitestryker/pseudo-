<?php 
$u = $_POST['uid'];
if (empty($u)){
echo "no data sent";
exit();
}
$comp = $_POST['comp'];
$identity = $_POST['username'];
$u = clean($u);
$comp = clean($comp);
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
             or die ("Couldn't connect to server.");
            $db = mysql_select_db("$database_name", $connection)
             or die("Couldn't select database.");
# check if users exist
$sql_check = mysql_query("SELECT uid FROM puser WHERE uid='$u'");
$results = mysql_num_rows($sql_check);

        if (($results > 0)) {
            if ($results > 0) {
             echo "error: please contact the site administrator";
            }
            exit(); // exit the script so that we do not create this account
        }
$sql = mysql_query("INSERT INTO puser (uid,identity,comp)
      			VALUES('$u','$identity','$comp')") or die (mysql_error());
        if (!$sql) {
        echo "There has been an error creating your account. Please contact the webmaster";
        exit();
        }
echo "successful"; 

// send the users a welcome PM 
$msgid = generateRandomString("5");
$deleted = "no";
$to = $identity;
$from = "Pseudo System";
$subject = "Welcome Aboard!";
$message = "Just wanted to Welcome You Aboard! \n";
$mesasge .= "and if you have any problems please email the System administrator \n";
$messsage .= "\n";
$message .= "              Best Regards,\n";
$messsage .= "\n";
$message .= "            Pseudo Sys Admin. \n";
$sql = mysql_query("INSERT INTO messages (msgid,to_user,from_user,deleted,subject,message)
      			VALUES('$msgid','$to','$from','$deleted','$subject', '$message')") or die (mysql_error());

function clean($var = null)
    {
        // sanitation
        $var = htmlspecialchars($var);
        $var = strip_tags($var);
        return $var;
    }
    
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