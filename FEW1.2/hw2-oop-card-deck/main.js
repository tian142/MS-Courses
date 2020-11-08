// This random card game is made from the guide provided by Blake Hearn:  https://medium.com/@blakeeh723/how-to-build-a-card-game-with-object-oriented-programming-c43cd2cadb3a
//defines a class of a Card with suit, rank, and value. This will be used in the create deck method in the Deck Class
class Card {
  constructor(suit, rank, value) {
    this.suit = suit;
    this.rank = rank;
    this.value = value;
  }
}
//defines class structure of a Deck
class Deck {
  constructor() {
    //initates a deck of cards as an empty Array to be populated in the createDeck() method below
    this.cards = [];
  }
  createDeck() {
    //defines the 4 suits to be pushed into the initiated cards Array above
    let suits = ['clubs', 'diamonds', 'hearts', 'spades'];
    //ranks the cards in accordance to the values declared in line 35
    let ranks = [
      'ace',
      '2',
      '3',
      '4',
      '5',
      '6',
      '7',
      '8',
      '9',
      '10',
      'jack',
      'queen',
      'king',
    ];
    //defines the 13 values from Ace(1) to King(13) suits to be pushed into the initiated cards Array above
    let values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
    //for loop to push both suits and values in to the deck in a organized manner (the forloop is nested because we have both suits and numbers)
    for (let i = 0; i < suits.length; i++) {
      for (let j = 0; j < ranks.length; j++) {
        this.cards.push(new Card(suits[i], ranks[j], values[j]));
      }
    }
  }

  //this function
  shuffleDeck() {
    //initiating 2 locations and a placeholder:
    let location1, location2, tmp;

    for (let i = 0; i < 1000; i++) {
      //randomizes 2 locations 1000 times:
      location1 = Math.floor(Math.random() * this.cards.length);
      location2 = Math.floor(Math.random() * this.cards.length);
      //places temp location of card 1:
      tmp = this.cards[location1];
      //swap postion of card 1 to card 2
      this.cards[location1] = this.cards[location2];
      //not sure what this means below:
      this.cards[location2] = tmp;
    }
  }
}

//creating a class for players to be made in a game scenario
class Player {
  constructor(name) {
    this.playerName = name;
    this.playerCards = [];
  }
}

//creating a class for a board in the event that there is a game going on
class Board {
  constructor() {
    //initates cardsInMiddle and players to be populated from the start function below:
    this.cardsInMiddle = [];
    this.players = [];
  }
  //create a game with 2 players
  start(playerOneName, playerTwoName) {
    //populates the players string with the 2 players:
    this.players.push(new Player(playerOneName));
    this.players.push(new Player(playerTwoName));
    //creating an instance of a Deck for the 2 players
    let d = new Deck();
    d.createDeck();
    //shuffles the deck created above
    d.shuffleDeck();
    //creating player[1 or 2]object with playerCards key and the first half of the shuffled card deck to player1 and the second half of the shuffled card deck to player 2
    //slice create a new array object: in this case, players[0].playerCards: [cards 1-26] , and players[1].playerCards: [cards 26-52]
    this.players[0].playerCards = d.cards.slice(0, 26);
    this.players[1].playerCards = d.cards.slice(26, 52);
  }
}

//Creating an instance of a game Board
let gameBoard = new Board();
//players are Marry and Mike
gameBoard.start('Marry', 'Mike');
//this will log the 2 players, and their methods of playerCards (26 random cards each)
console.log(gameBoard.players);
