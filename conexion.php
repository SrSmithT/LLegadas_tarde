<?php

$fecha_tarde = $_POST['fecha_tarde'];
$id_estudiante = $_POST['id_estudiante'];
$hora_llegada_tarde = $_POST['hora_llegada_tarde'];


$conexion = mysqli_connect('localhost', 'root', 'mysqlpasswordAAA1_', 'pruebas')
    or die(mysql_error($mysqli));

if ($conexion) {
    die("Error de conexión" . mysqli_connect_error());
}

$fecha_tarde = mysqli_real_escape_string($conexion, $fecha_tarde);
$id_estudiante = mysqli_real_escape_string($conexion, $id_estudiante);
$hora_llegada_tarde = mysqli_real_escape_string($conexion, $hora_llegada_tarde);


$consulta = "INSERT INTO llegadas_tarde_p1 (fecha_tarde, id_estudiante, hora_llegada_tarde) VALUES ('$fecha_tarde', '$id_estudiante', '$hora_llegada_tarde')";

if (mysqli_query($conexion, $consulta)) {
    echo "Los datos se insertaron correctamente";
} else {
    echo "Error al insertar los datos" . mysqli_error($conexion);
}

mysqli_close($conexion)

    ?>