function play_game() {
  var form = document.getElementById("gameForm");
  form.addEventListener("click", function(event) {
    var user_choice = event.target.value;
    if (user_choice) {
      var result = fight(user_choice);
      document.getElementById("result").innerText = result;
    }
  });
}


function fight(user_choice) {
  var computer_choice = Math.floor(Math.random() * 3);
  var result;

  // 0 is rock, 1 is paper, 2 is scissors
  if (
    (computer_choice === 0 && (user_choice === "p" || user_choice === "P")) ||
    (computer_choice === 1 && (user_choice === "s" || user_choice === "S")) ||
    (computer_choice === 2 && (user_choice === "r" || user_choice === "R"))
  ) {
    result = "You win!";
  } else if (
    (computer_choice === 0 && (user_choice === "r" || user_choice === "R")) ||
    (computer_choice === 1 && (user_choice === "p" || user_choice === "P")) ||
    (computer_choice === 2 && (user_choice === "s" || user_choice === "S"))
  ) {
    result = "It's a tie!";
  } else {
    result = "You lose!";
  }

  return result;
}

