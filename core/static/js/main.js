function getPics() {} //just for this demo
const imgs = document.querySelectorAll('.card img');
const fullPage = document.querySelector('#fullpage');
const isHidden = () => fullPage.classList.contains("box--hidden");

const exampleModal = document.getElementById('exampleModal')

imgs.forEach(img => {
  img.addEventListener('click', function() {
    fullPage.style.backgroundImage = 'url(' + img.src + ')';
    fullPage.style.display = 'block';
    fullPage.style.opacity = '1';
  });
});


window.onpopstate = function(event) {
    event.preventDefault()
    fullPage.style.display = "none";
    // DO some other action besides going back
    return false
  }

let args = [16, 65, 68];
let arrChars = [];

document.addEventListener('keydown', function(event) {
    if (event.repeat) return;
    arrChars.push(event.keyCode);
});

document.addEventListener("keyup", function (event) {
    if (arrChars.length == 0) return;

    let runFunc = true;
    for (let arg of arrChars) {
      if (arrChars.length === 3){
        if (!args.includes(arg)) {
            runFunc = false;
            break;
        }
      }
      else {
        runFunc = false;
        break;
      }
    }
    if (runFunc) func();

    arrChars.length = 0;
});

function func () {
    $(exampleModal).modal("show");
    // var my_route = "{{ url_for('add_new_post') }}";
    // window.location.href = my_route;
}


exampleModal.addEventListener('show.bs.modal', event => {
  // Button that triggered the modal
  const button = event.relatedTarget
  // Extract info from data-bs-* attributes
  const recipient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  const modalTitle = exampleModal.querySelector('.modal-title')
  const modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = `New message to ${recipient}`
  modalBodyInput.value = recipient
})