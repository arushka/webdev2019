// Write your code below
var bobsFollowers=['Rob','Jack','Ted','Mark'];
var tinasFollowers=['Rob','Ted','Anne'];
var mutualFollowers=[];
for (let i=0;i<bobsFollowers.length;i++){
  for (let j=0;j<tinasFollowers.length;j++){
    if (bobsFollowers[i]===tinasFollowers[j]){
      mutualFollowers.push(bobsFollowers[i]);
    }
  }
}
