function play_game(user_choice) {
  var result = fight(user_choice);
  document.getElementById("result").innerText = result;
}

function fight(user_choice) {
  var computer_choice = Math.floor(Math.random() * 3);
  var result;

  // 0 is rock, 1 is paper, 2 is scissors
  if (
    (computer_choice === 0 && user_choice === "p") ||
    (computer_choice === 1 && user_choice === "s") ||
    (computer_choice === 2 && user_choice === "r")
  ) {
    result = "You win!";
  } else if (
    (computer_choice === 0 && user_choice === "r") ||
    (computer_choice === 1 && user_choice === "p") ||
    (computer_choice === 2 && user_choice === "s")
  ) {
    result = "It's a tie!";
  } else {
    result = "You lose!";
  }

  return result;
}

