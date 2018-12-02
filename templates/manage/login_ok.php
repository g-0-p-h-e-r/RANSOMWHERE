<?php
session_start();
$id="ruid"
$pw="rupw"

if($_POST['id'] === $id && $_POST['pw'] === $pw){
	$_SESSION["ck_login"] = true;
	header('Location: /menu')
}
else if($_POST['id'] != $id or $_POST['pw'] != $pw){?>
	<script>alert('fucking !!!');location.href='./admin_loginpage.html';<script>
}
<?php ?>
