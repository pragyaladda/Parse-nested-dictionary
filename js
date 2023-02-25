function loadJSON(callback) {   
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");
  xobj.open('GET', 'data.json', true);
  xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") {
          callback(xobj.responseText);
        }
  };
  xobj.send(null);
}

loadJSON(function(data) {
  jsonData = JSON.parse(data);
  displayData();
});
display.js:

javascript
Copy code
function displayData() {
  var output = document.getElementById("output");
  output.innerHTML = "<h2>JSON Data:</h2>" +
    "<p>Name: " + jsonData.name + "</p>" +
    "<p>Age: " + jsonData.age + "</p>" +
    "<p>Email: " + jsonData.email + "</p>" +
    "<p>Address: " + jsonData.address.street + ", " + jsonData.address.city + ", " + jsonData.address.state + " " + jsonData.address.zip + "</p>" +
    "<p>Phone: " + jsonData.phone[0].type + ": " + jsonData.phone[0].number + ", " + jsonData.phone[1].type + ": " + jsonData.phone[1].number + "</p>";
}
In this example, we define a global variable jsonData in data.js, and set its value to the parsed JSON data in index.js using the loadJSON() function. We then call displayData() in index.js, which is defined in display.js and uses the jsonData global variable to display the JSON data on the page.

When you open index.html in a web browser, it should display the same output as the previous example. However, the code has been split into multiple JS files, and the global variable jsonData is accessed across them.




