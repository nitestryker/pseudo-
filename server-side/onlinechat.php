<?php
$uid = $_POST['username'];
$uid = clean($uid);

// online in chat 
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
             or die ("Couldn't connect to server.");
            $db = mysql_select_db("$database_name", $connection)
             or die("Couldn't select database.");
$online = 1;
 mysql_query("UPDATE puser SET onlinechat='$online' WHERE identity ='$uid'");
function clean($var = null)
    {
        // sanitation
        $var = htmlspecialchars($var);
        $var = strip_tags($var);
        return $var;
    }
$dbhost = "";
$dbusername = "";
$dbpasswd = "";
$database_name = "";
$connection = mysql_connect("$dbhost", "$dbusername", "$dbpasswd")
     or die ("Couldn't connect to server.");
   	    $db = mysql_select_db("$database_name", $connection)
               or die("Couldn't select database.");
$sql = "SELECT * FROM  puser WHERE onlinechat = '1'";
$result = mysql_query($sql);
while ($row = mysql_fetch_array($result)) {
$username = $row['identity'];
print "  $username\n";
}
if ($username != uid && $username == "" ){
  print "no other users online\n";
}
?>