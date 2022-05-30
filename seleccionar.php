<?php
 
$metodo = $_POST ['accion'];
$eje = $_POST ['eje'];
$c = $_POST [ 'constante' ];
$n = $_POST [ 'n' ];
$num=$_POST [ 'numero' ];

if($c==""){
    $c=1;
}
$ejecutar='python graficar.py '.$metodo." ".$eje." ".$c." ".$num." ".$n;

$command = escapeshellcmd("$ejecutar");
$output = shell_exec($command);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<font face="arial, verdana">
    <?php
        for ($i=0; $i < $output; $i++) { 
            echo '<img src="grafica'.$i.'.png"><br>';
        }
    ?>
    <form action="modificar.php" method='post'>
        <input type="text" name="nn" value="<?php echo $output;?>" readonly>
        <input type="text" name="ene" value="<?php echo $n;?>" readonly>
        <input type="submit" value="Continuar editando">
        <a href="index.html">Regresar al inicio</a>
    </form>
</font>
</body>
</html>