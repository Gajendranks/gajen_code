<html>
<head>
<center>
<script>
// This function converts a number to words
function numToWords(num) {
  // Define arrays of words for each group of digits
  var ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  var teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
               "seventeen", "eighteen", "nineteen"];
  var tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"];
  var bigs = ["", "thousand", "million", "billion"];

  // Convert the number to a string and reverse it
  var numString = num.toString().split("").reverse().join("");

  // Split the string into groups of three digits
  var groups = [];
  for (var i = 0; i < numString.length; i += 3) {
    groups.push(numString.slice(i, i + 3));
  }

  // Convert each group to words
  var words = [];
  for (var j = 0; j < groups.length; j++) {
    var group = groups[j];
    var groupWords = [];

    // Handle the hundreds digit
    if (group[2]) {
      groupWords.push(ones[group[2]] + " hundred");
    }

    // Handle the tens and ones digits
    if (group[1] == 1) {
      // Use the teens array for numbers from 10 to 19
      groupWords.push(teens[group[0]]);
    } else {
      // Use the tens and ones arrays for other numbers
      groupWords.push(tens[group[1]]);
      groupWords.push(ones[group[0]]);
    }

    // Add the bigs suffix for the group
    groupWords.push(bigs[j]);

    // Join the words with spaces and add them to the words array
    words.push(groupWords.filter(word => word).join(" "));
  }

  // Reverse the words array and join it with commas and spaces
  return words.reverse().filter(word => word).join(", ");
}

// This function gets the input value and displays the output
function convert() {
  // Get the input element and its value
  var input = document.getElementById("number");
  var num = input.value;

  // Validate the input value
  if (isNaN(num)) {
    alert("Please enter a valid number");
    input.focus();
    return;
  }

  if (num < 0 || num > 999999999) {
    alert("Please enter a number between 0 and 999999999");
    input.focus();
    return;
  }

  // Convert the number to words and display it in the output element
  var output = document.getElementById("output");
  var words = numToWords(num);
  output.innerHTML = words;
}
</script>
</head>
<body bgcolor="pink">
<h1>Number to Words Converter</h1>
<p>Enter a number between 0 and 999999999 and click Convert</p>
<input type="text" id="number" placeholder="Enter a number">
<button onclick="convert()">Convert</button>
<p id="output"></p>
</body>
</center>
</html>
