<?php
if(isset($_POST [ 'num' ])){
    $num=$_POST [ 'num' ];
}
if(isset($_POST [ 'nn' ])){
    $num=$_POST [ 'nn' ];
}
if(isset($_POST [ 'ene' ])){
    $num=$_POST [ 'nn' ];
}

if($num==0){
    $cont=$_POST [ 'contador' ];
    $n=$cont/2;
    $ruta="poligono.txt";
    $archivo = fopen($ruta, "w") or die("Ocurrio un error al abrir el archivo");
    fwrite($archivo, "x y\n") or die("No se puede escribir en el archivo");
    fclose($archivo);
    for ($i = 0; $i < $cont; $i++) {
        $h = $_POST [$i];
        $archivo = fopen($ruta, "a") or die("Ocurrio un error al abrir el archivo");
        if($i%2==0){
            $cadena=$h." ";
            fwrite($archivo, "$cadena") or die("No se puede escribir en el archivo");
        }else{
            $cadena=$h."\n";
            fwrite($archivo, "$cadena") or die("No se puede escribir en el archivo");
        }
        fclose($archivo);
    }
}else{
    $n=$_POST [ 'ene' ];
}

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
    <form action="seleccionar.php" method="post">
        
        <p>Ingresa la accion</p>
        
        <label>
            <input type="radio" name="accion" value="1" checked> Reflectar
        </label>
        <label>
            <input type="radio" name="accion" value="2"> Expandir
        </label>
        <label>
            <input type="radio" name="accion" value="3"> Cortar
        </label>
        <label>
            <input type="radio" name="accion" value="4"> Rotar
        </label>
        <br>
        <p>Ingresa el eje</p>
        <label>
            <input type="radio" name="eje" value="x" checked> x
        </label>
        <label>
            <input type="radio" name="eje" value="y"> y
        </label>
        <br>
        <p>Ingresa la constante</p>
        <label>
            <input type="text" name="constante" value=1>
        </label>
        <input type="hidden" name="n" value="<?php echo $n;?>" readonly>
        <input type="hidden" name="numero" value="<?php echo $num;?>" readonly>
        <br><br>
        <input type="submit" value="Enviar">
        <a href="index.html">Regresar al inicio</a>
    </form>
    
</font>
</body>
</html>