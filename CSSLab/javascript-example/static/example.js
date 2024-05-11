function changeColor() {
  the_heading = document.getElementById("hello");
  the_heading.style.color = "red";
  console.log("I just changed the color to: " + the_heading.style.color)  
}

function fight(user_choice){
	potential_position = ['Rock', 'Paper', 'Scissors'];
	computer_choice = Math.floor(Math.random() * 3);

	//0 is rock 1 is paper 2 scissors
	if (computer_choice == 0 && (user_choice == 'p' || user_choice == 'P')):
		return("Rock loses to Paper, you win!!!");
	else if (computer_choice == 1 && (user_choice == 's' || user_choice == 'S')):
		return("Paper loses to Scissors, you win!!!");
	else if (computer_choice == 2 and (user_choice == 'r' or user_choice == 'R')):
		return("Scissors loses to Rock, you win!!!");
	else if (computer_choice == 0 && (user_choice == 'r' || user_choice == 'R')):
		return("It's a tie!");
	else if (computer_choice == 1 && (user_choice == 'p' || user_choice == 'p')):
                return("It's a tie!");
	else if (computer_choice == 2 && (user_choice == 's' || user_choice == 'S')):
                return("It's a tie!");
	else:
		return("You lose");

}

function play_game():
	while true:
		user = prompt("Rock, Paper, or Scissors? You can just write r, p, or s: ");
		fight(user)
		play_again = prompt("Do you want to play again? (y/n): ");
		if play_again.lower() != 'y':
			return("Thanks for playing!");
			break


play_game()
