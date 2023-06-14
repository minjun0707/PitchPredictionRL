function csv() {


    
    const number = [];
    const name = [];

    fetch('ID.csv')
  .then(response => response.text())
  .then(text =>{
    for(var i = 0 ; i< 694 ; i++) {
    const row = text.slice(0, text.indexOf('\n')).split(",");
    number.push(row[0])
    name.push(row[1])
    console.log(row)}
  })

  
//   var str = csvToText
//   const id = csvToText.slice(1);
  
  
  
}