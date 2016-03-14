object binary_search { 
  
  def binary_search_i (ls: Array[Int], item: Int): Boolean = {
    var first = 0;
    var last = ls.length - 1
    while (first <= last) {
      val midpoint = (first + last) /2
      if (ls(midpoint) == item)
        return true;
      else if (ls(midpoint) > item)
        last = midpoint - 1;
      else
         first = midpoint + 1;
    }
    false
  }

  //def binary_search_r (ls: Array[Int], item: Int): Boolean = {
    
  //}

//def binary_search_f (ls: Array[Int], item: Int) Int = {
//}
  
  def main (args: Array[String]) {
    val ls = Array(1,2,3,5,9);
    print ("Item list: [");
    var i = 0;
    for (i <- 0 to ls.length - 1) {
      print (ls(i) + " ");
    }
    println ("]");
      
    print ("Item to find: ");
    val item = Console.readInt;
    if (binary_search_i (ls, item)) 
      println ("Item is found.");
    else 
      println ("Item is not found.");
  }
}