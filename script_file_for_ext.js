window.onload = function() { //when the browser loads, this activates
    var fileInput = document.getElementById('fileInput'); 
    var fileDisplayArea = document.getElementById('fileDisplayArea'); // these both are just html elements 
    let nav_wrapper_indicator = document.getElementById('nav_wrapper');
    nav_wrapper_indicator.style.display = "none";

fileInput.addEventListener('change', function(e) { //activated when user select a file
    var file = fileInput.files[0]; //[0] gets the list of file data (size,name,type,etc)
    var textType = /text.*/; //used later to test if == text
    nav_wrapper_indicator.style.display = "block";


    // ---OPTION 1----
    const reader = new FileReader();
    reader.readAsText(file); // 1- reads the file 

    reader.onload = function (e) { // 2- gets from 1- and calls function to make array 
        const text = e.target.result;
        const PeerGroupData = csvToArray(text);
        loadTableData(PeerGroupData);

        // console.log(PeerGroupData);
        // let array_headers = Object.keys(PeerGroupData[0]);
        // console.log(array_headers[1]);
        // console.log(array_headers.length-1);

        };   

        
    // Functions 
    function csvToArray(str, delimiter = ";") { // create two arrays called headers and rows
        const headers = str.slice(0, str.indexOf("\n")).split(delimiter);// slice from start of text to the first \n index
        const rows = str.slice(str.indexOf("\n") + 1).split("\n");// slice from \n index + 1 to the end of the text

        const arr = rows.map(function (row) { //create the array of objects -> this is the array 
            const values = row.split(delimiter);
            const el = headers.reduce(function (object, header, index) {
                object[header] = values[index];
                return object}, {});
            return el;         
            });
        return arr;
        // console.log(arr)
        };

    function loadTableData(PeerGroupData) {
        const tableBody = document.getElementById('tableData');
        let dataHtml = '';
        let array_headers = Object.keys(PeerGroupData[0]);
        let array_data = Object.values(PeerGroupData);
        // console.log(array_data[0]['Balance'])
        // unshift and create full set
        let first_row ={}
        for (var i = 0; i < array_headers.length; i++) {
            first_row[array_headers[i]] = array_headers[i];
        };
        array_data.unshift(array_headers)
        
        // console.log(PeerGroupData.length,array_data.length)
        // console.log(array_data)


        // define tb
        for(var i=0; i<array_data.length; i++){ //rows
            var row=document.createElement("tr");
            let array_headersX = Object.values(array_data[i]);
            // console.log(i)
            // console.log(array_headersX)
            for (var j=0; j < array_headers.length; j++){  //cols
                var cell = document.createElement("td");
                var cellText = document.createTextNode(array_headersX[j]);
                if(i == 0){
                    var cell = document.createElement("th");
                    cellText = document.createTextNode(array_headers[j]);
                };
                cell.append(cellText);
                row.append(cell);
            };
        tableBody.append(row);
        };

        // for(let group of PeerGroupData) {
        //     dataHtml += `<tr><td>${group.Last_Name}</td><td>${group.Last_Name}</td></tr>`;
        // }
        // tableBody.innerHTML = dataHtml
        };

    });
};

function openCity(evt, tabLink) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabLink).style.display = "block";
  evt.currentTarget.className += " active";
};

function myFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  
  for (i = 1; i < tr.length; i++) {
    // td = tr[i].getElementsByTagName("td")[2];
    // console.log(td)
    td = tr[i];//.getElementsByTagName("td")[2];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
          
        var input2, filter2, txtValue2;
        input2 = document.getElementById("myInput2");
        filter2 = input2.value.toUpperCase();
        
        if (filter2.length > 0) {
            txtValue2 = td.textContent || td.innerText;
            if (txtValue2.toUpperCase().indexOf(filter2) > -1) { //searches input in row array. so if found then 
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        };
          
      } else {
        tr[i].style.display = "none";
      }
    }       
  }

};
