const groceryList = ['orange juice', 'bananas', 'coffee beans', 'brown rice', 'pasta', 'coconut oil', 'plantains'];
//remove the first element
groceryList.shift();

//add to the first place
groceryList.unshift('popcorn');

//pick some elements from index 1 to 4
console.log(groceryList.slice(1,4));

console.log(groceryList);

const pastaIndex=groceryList.indexOf('pasta');
console.log(pastaIndex);