function getUserChoice(userInput){
  userInput.toLowerCase();
  if(userInput==='rock'|| userInput==='paper' || userInput==='scissors' || userInput==='bomb'){
    return userInput;
    
  }else{
    console.log('Error!');
  }
}
function getComputerChoice(){
 var num=Math.floor(Math.random()*3);
  if(num===0){
    return 'rock';
  } else if(num===1){
    return 'paper';
  } else if(num===2){
    return 'scissors';
  }
}
function determineWinner(userChoice,computerChoice){
  if(userChoice===computerChoice){
    return 'Game was a tie';
  }
  if (userChoice==='rock'){
    if (computerChoice==='paper'){
      return 'Computer is a Winner!';
    }else if (computerChoice==='scissors'){
      return 'User is a Winner!'
    }
  }
    if (userChoice==='paper'){
    if (computerChoice==='rock'){
      return 'User is a Winner!';
    }else if (computerChoice==='scissors'){
      return 'Computer is a Winner!'
    }
  }
    if (userChoice==='scissors'){
    if (computerChoice==='rock'){
      return 'Computer is a Winner!';
    }else if (computerChoice==='paper'){
      return 'User is a Winner!'
    }
  }
  if (userChoice==='bomb'){
    return 'User is a Winner!!!'
  }
}
function playGame(){
  var userChoice=getUserChoice('bomb');
  var computerChoice=getComputerChoice();
  console.log(userChoice,computerChoice);
  console.log(determineWinner(userChoice,computerChoice));
}
playGame();