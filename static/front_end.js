'use strict'

const BASE_URL="http://localhost:5000/api/";
const $cupcakeList = $('#cupcake_list');

// async function on load
  //make await axios request to API to get all cupcakes
  // loop through list of cupcakes
  // create a new list item element for each
  // append list item to UL in HTML template

async function showCupcakesOnStart(){

  let response = await axios.get(`${BASE_URL}cupcakes`);
  let cupcakes = response.data.cupcakes;

  for (let cupcake of cupcakes){
    let $cupcakeDiv = $('<div>');
    let $cupcakeImg = $('<img>').attr("src", cupcake.image);
    let $cupcakeFlavor = $('<h3>').text(cupcake.flavor);
    let $cupcakeRating = $('<h3>').text(cupcake.rating);
    let $cupcakeSize = $('<h3>').text(cupcake.size);
    $cupcakeDiv.append($cupcakeFlavor)
      .append($cupcakeImg)
      .append($cupcakeRating)
      .append($cupcakeSize)
    let $cupcakeListItem = $('<li>').append($cupcakeDiv);
    $cupcakeList.append($cupcakeListItem);
  }

}

showCupcakesOnStart();