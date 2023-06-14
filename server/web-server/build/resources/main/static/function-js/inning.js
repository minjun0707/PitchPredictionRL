  // Select increment and decrement buttons
  const incrementCount = document.getElementById("increment-count");
  const decrementCount = document.getElementById("decrement-count");
  
  // Select total count
  const totalCount = document.getElementById("total-count");
  
  // Variable to track count
  var count = 1;
  
  // Display initial count value
  totalCount.innerHTML = count;
  
  // Function to increment count
  const handleIncrement = () => {
    if (count ==9){
      return;
    }
    count++;
    totalCount.innerHTML = count;
  };
  
  // Function to decrement count
  const handleDecrement = () => {
    if(count == 1){
      retrun;
    }
  
    count--;
    totalCount.innerHTML = count;
  };
  
  // Add click event to buttons
  incrementCount.addEventListener("click", handleIncrement);
  decrementCount.addEventListener("click", handleDecrement);