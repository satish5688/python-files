// Setup
// const recordCollection = {
//     2548: {
//       albumTitle: "Slippery When Wet",
//       artist: "Bon Jovi",
//       tracks: ["Let It Rock", "You Give Love a Bad Name"],
//     },
//     2468: {
//       albumTitle: "1999",
//       artist: "Prince",
//       tracks: ["1999", "Little Red Corvette"],
//     },
//     1245: {
//       artist: "Robert Palmer",
//       tracks: [],
//     },
//     5439: {
//       albumTitle: "ABBA Gold",
//     },
//   };
  
//   // Only change code below this line
//   function updateRecords(records, id, prop, value) {
//     if (value == "") {
//       delete records[id][prop]
//     }
//      else if (value == "Free") {
//       records[id][prop] = [value];
//     }
//     else if (prop == "tracks") {
//       records[id][prop] = [value];
//     }
//      else {
//       records[id][prop] = value;
//     }
//     return records;
//   }
  
//   updateRecords(recordCollection, 5439, 'artist', 'ABBA');
//   updateRecords(recordCollection, 5439, "tracks", "Take a Chance on Me");
//   updateRecords(recordCollection, 2548, "artist", "")
//   updateRecords(recordCollection, 2468, "tracks", "1999")
//   console.log(recordCollection);



function multiplyAll(arr) {
  let product = 1;
  for (let s=0; s<arr.lengt; s++){
    for(let v=0; v<arr[i].length; v++){
      product*=v
    }
  }
  return product;
}

multiplyAll([[1, 2], [3, 4], [5, 6, 7]]);