<?php
    $firstName = $_POST['firstName'];
    $conEmail = $_POST['conEmail'];
    $conPhone = $_POST['conPhone'];
    $conSubject = $_POST['conSubject'];
    $conMessage = $_POST['conMessage'];

    ini_set( 'display_errors', 1 );
    error_reporting( E_ALL );

    # FIX: Replace this email with recipient email
    $to = "theme.junction.live@gmail.com";

    $subject = $conSubject;
    $txt = "You have a new message from your ImmiPress website Contact Form\n=============================\n" . "First Name: " . $firstName . "\nEmail: " .$conEmail. "\nPhone: ".$conPhone. "\nSubject:" .$conSubject. "\nMessage:" .$conMessage;
    
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