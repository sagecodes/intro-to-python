var guess;
var message;
var tries = 0;

function game(numberRange) {
  var answer = Math.floor(Math.random() * numberRange) +1;
  while (answer != guess) {
    guess = prompt("What is your guess? " + message);
    if (guess < answer) {
      message = "your guess is too low";
  } else if (guess > answer) {
    message = "your guess is too high";
  } else {
    message = "I think you did something wrong"
  } 
  alert("you won")
}