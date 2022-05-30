function crear(){
    
    document.getElementById("puntos").innerHTML = "";
    document.getElementById("mostrarP").innerHTML = "";
    
    var i, j;
    
    var n=0;

    n=document.getElementById("n").value;

    var HTML = "<table border=0 width=80%>";

    


    for(i=0; i<n; i++){
        
        HTML += "<tr>";
        for(j=0;j<2;j++){
            HTML += "<td align=center>"+'<input type="text" id="x'+i+'_'+j+'" onkeypress="return valideKey(event, this);" style="width: 80px;" > </td>';
        }
    
    }
    


    HTML += "</table>";
    HTML += '<input id="btnCalcular" type="button" value="Aceptar" onclick="calcular()" ></input>'
    document.getElementById("puntos").innerHTML = HTML;

}




function calcular(){
    document.getElementById("mostrarP").innerHTML = "";

    var n=0;

    

    n=document.getElementById("n").value;

    var contador=0;
    var contador0=0;
    var contador02=0;
    
    /******************* */
    for(i=0; i<n; i++){
        for(j=0;j<2;j++){
            if(document.getElementById("x"+i+"_"+j).value=="" || document.getElementById("x"+i+"_"+j).value=="-"){
                contador++;
            }else if(document.getElementById("x"+i+"_"+j).value==0){
                contador0++;
            }
        }

    }

    for (j = 0;  j< 2; j++) {
        for (i = 0; i < n; i++) {
            if(document.getElementById("x"+i+"_"+j).value==0){
                contador02++;
            }
            
        }
        
    }
    if(contador>0||contador0==n*2){
        alert("rellena todas las ecuaciones con numeros");
        return false;
    }

    //********************** */


    var matriz= new Array(n);

    var i, j;

    for(i=0; i<n; i++){
        matriz[i]= new Array(2);
        for(j=0; j<2;j++){
            matriz[i][j] = document.getElementById('x'+i+'_'+j+'').value;
        }
    }


    var HTML = "<table border=0 width=80%>";

    for(i=0; i<matriz.length; i++){
        
        HTML += "<tr>";
        for(j=0;j<matriz[i].length;j++){
            
            HTML += '<td align=center>'+matriz[i][j]+'</td>';
            
            
        }
    
    }
    
    HTML += "</tr></table>";
    HTML+= "<form action='modificar.php' method='post'>"
    var cont=0;
    for(i=0; i<n; i++){
        for(j=0;j<2;j++){
            HTML += '<input type="hidden" name="'+cont+'" style="width: 80px;" value="'+matriz[i][j]+'" readonly>';
            cont++;
        }
    
    }
    HTML += '<input type="hidden" name="contador" style="width: 80px;" value="'+cont+'" readonly>';
    HTML += '<input type="hidden" name="num" style="width: 80px;" value="0" readonly>';
    HTML+= "<input type='submit' value='Confirmar'>"
    HTML+= "</form>"
    
    document.getElementById("mostrarP").innerHTML = HTML;

    
    


}

function WriteFile(miCadenaDeTexto){
    
    /*var fso  = CreateObject("Scripting.FileSystemObject");
    var fh = fso.CreateTextFile("Test.txt", true); 
    fh.WriteLine(miCadenaDeTexto); 
    fh.Close();*/ 
    var arrayData = new Array();
    var archivo = new XMLHttpRequest();
    var ruta= "poligono.txt";
    var suma=0;
    archivo.open("GET", ruta, false);
    archivo.send(null);
    var txt=archivo.responseText;
    for (let i = 0; i < txt.length; i++) {
        arrayData.push(txt[i]);
    }
    arrayData.forEach(function(data) {
        console.log(data);
        suma+=parseFloat(data);
    });
    if(suma==0){
        console.log("Pon algo");
    }else{
        console.log("la suma es:"+suma);
    }

/*
x y
3.0 8.2
2.0 17.8
3.3 9.919999999999998
*/


}