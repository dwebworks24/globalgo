<?php
    $firstName = $_POST['firstName'];
    $conEmail = $_POST['conEmail'];
    $conCountry = $_POST['conCountry'];
    $conVisa = $_POST['conVisa'];
    $subject = "Check Your Eligibility Form 2 (Hero Section)";

    ini_set( 'display_errors', 1 );
    error_reporting( E_ALL );

    # FIX: Replace this email with recipient email
    $to = "theme.junction.live@gmail.com";

    $subject = $subject;
    $txt = "You have a new message from your ImmiPress website Check Your Eligibility Form 2 (Hero Section)\n=============================\n" . "First Name: " . $firstName . "\nEmail: " .$conEmail. "\nCountry:" .$conCountry. "\nVisa:" .$conVisa;
    
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