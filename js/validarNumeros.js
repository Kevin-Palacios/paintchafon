//q:)->-</:
function valideKey(evt,input) {
    /*
    var code = evt.which ? evt.which : evt.keyCode;
    if (code == 8) {
        return true;
    } else if ((code >= 48 && code <= 57)) {
        //codigo ascii numeros
        return true;
    }  else {
        return false;
    }
    */

    
    // Backspace = 8, Enter = 13, ‘0′ = 48, ‘9′ = 57, ‘.’ = 46, ‘-’ = 43
    var key = window.Event ? evt.which : evt.keyCode;
    var chark = String.fromCharCode(key);
    if(key==45){
        var tempValue = input.value+chark+0;
    }else{
        var tempValue = input.value+chark;
    }
    


    if(key >= 48 && key <= 57){
        if(filter(tempValue)=== false){
            return false;
        }else{       
            return true;
        }
    }else{
            if(key == 8 || key == 13 || key == 0) {     
                return true;              
            }else if(key == 46){
                if(filter(tempValue)=== false){
                    return false;
                }else{       
                    return true;
                }
            }else if(key==45){
                
                if(filter(tempValue)=== false){
                    return false;
                }else{       
                    return true;
                }
            }else{
                return false;
            }
    }
    }
    
    function filter(__val__){
        
    var preg = /^(\-?[0-9]+\.?[0-9]{0,10})$/; 
    //var preg = /^([0-9]+\.?[0-9]{0,10})$/; 
    if(preg.test(__val__) === true){
        return true;
    }else{
        return false;
    }
      
    
}