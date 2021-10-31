let outputScreen = document.querySelector('#outputScreen');
function display(num){
    outputScreen.value+=num;
}

function Calculate(){
    try{
        outputScreen.value=eval(outputScreen.value);
    }
    catch(alert){
        alert("Invalid Input");
    }
}

function Clear(){
    outputScreen.value='';
}

function Del(){
    outputScreen.value=outputScreen.value.slice(0,-1);
}
