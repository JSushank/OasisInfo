let display = document.getElementById('calculate');
let buttons = Array.from(document.getElementsByClassName('button'));
document.getElementById('equal').addEventListener('click', function(e) {
    if (display.value === '') {
      display.value = "Please enter";
    } else {
      let answer = eval(display.value);
      display.value = answer;
    }
});
buttons.map( button => {
    button.addEventListener('click', (e) => {
        switch(e.target.innerText){
            case 'C':
                display.innerText = '';
                break;
                case '=':
                    try {
                        const result = eval(display.innerText);
                        if (isNaN(result) || !isFinite(result)) {
                            display.innerText = "Error";
                        } else {
                            display.innerText = result;
                        }
                    } catch (error) {
                        display.innerText = "Error";
                    }
                    break;
                
                    case '←':
                        if (display.innerText){
                            display.innerText = display.innerText.slice(0, -1);
                        }
                        break;
                    
            default:
                display.innerText += e.target.innerText;
                
        }
    });
});