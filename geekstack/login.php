<?php
$host="localhost";
$user="root";
$password="";
$db="quotescomments";
 mysql_connect($host,$user,$password);
mysql_select_db($db);
if(isset($_post['username'])){
    $uname=$_post['username'];
    $password=$_post['password'];
    $sql="select * from loginform "
}