let correctAnswerButtons = document.querySelectorAll('#correct')
let incorrectAnswerButtons = document.querySelectorAll('#incorrect')

// document.querySelector('button').addEventListener('click', function() {
//     document.querySelector()
// } )

// function changeColor(correctAnswer) {
//     correctAnswer.addEventListener('click', () => {
//         correctAnswer.style.color='green';
//     })
// }

for ( let button of correctAnswerButtons) {
    button.addEventListener('click', (event) => {
        button.style.color = 'white'
        button.style.backgroundColor = 'green'
    })
}

for ( let button of incorrectAnswerButtons) {
    button.addEventListener('click', (event) => {
        button.style.color = 'white'
        button.style.backgroundColor = 'red'
    })
}