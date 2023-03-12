function checkPhone(){
    let phone = document.getElementById("phone_number");
    if(phone.validity.valid == false){
        phone.setCustomValidity("Please enter a number in ###-###-#### format.");
    }
}

function inputPhone(){
    let phone = document.getElementById("phone_number");
    phone.setCustomValidity("");
}

function showHelp(){
    let help = document.getElementById("help");
    help.style = "display: inline";
}