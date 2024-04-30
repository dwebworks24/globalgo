<?php
    $firstName = $_POST['firstName'];
    $lastName = $_POST['lastName'];
    $conEmail = $_POST['conEmail'];
    $conPhone = $_POST['conPhone'];
    $conMaritalStatus = $_POST['conMaritalStatus'];
    $conOccupation = $_POST['conOccupation'];
    $conCountry = $_POST['conCountry'];
    $conVisa = $_POST['conVisa'];
    $subject = "Check Your Eligibility Form 1";

    ini_set( 'display_errors', 1 );
    error_reporting( E_ALL );

    # FIX: Replace this email with recipient email
    $to = "theme.junction.live@gmail.com";

    $subject = $subject;
    $txt = "You have a new message from your ImmiPress website Check Your Eligibility Form 1\n=============================\n" . "First Name: " . $firstName . "\nLast Name: " .$lastName. "\nEmail: " .$conEmail. "\nPhone: ".$conPhone. "\nMarital Status:" .$conMaritalStatus. "\nOccupation:" .$conOccupation. "\nCountry:" .$conCountry. "\nVisa:" .$conVisa;
    
    $headers = 'From: ImmiPress' . "\r\n" .
    "Reply-To:" . $conEmail . "\r\n" .
    'X-Mailer: PHP/' . phpversion();
  
    if(mail($to,$subject,$txt,$headers))
    {
        echo "Y";
    }
    else{
        echo "N";
    }
    
?>