<?php
error_reporting(E_ALL);
$uid = $_POST['uid'];
$comp = $_POST['comp'];

$uid = clean($uid);
$comp = clean($comp);

$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
             or die ("Couldn't connect to server.");
            $db = mysql_select_db("$database_name", $connection)
             or die("Couldn't select database.");
if ((!$uid) || (!$comp)) {
         exit();
        }
$sql = mysql_query("SELECT * FROM puser WHERE uid='$uid' AND comp='$comp'");
$login_check = mysql_num_rows($sql);
        if ($login_check > 0) {
        while ($row = mysql_fetch_array($sql)) {
        foreach ($row AS $key => $val) {
         $$key = stripslashes($val);
                }
         $username = $row['identity'];
         }
        echo $username;
        } else {
        echo "failed"; 
        }

// update online status 
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
             or die ("Couldn't connect to server.");
            $db = mysql_select_db("$database_name", $connection)
             or die("Couldn't select database.");
$online = 1;
 mysql_query("UPDATE puser SET online='$online' WHERE uid ='$uid'");
function clean($var = null)
    {
        // sanitation
        $var = htmlspecialchars($var);
        $var = strip_tags($var);
        return $var;
    }

?>