#include <iostream>
using namespace std;
 
bool binary_search_r (int ls[], int first, int last, int item) {
  if (last < first) 
    return false;
  int midpoint = (first + last) / 2;
  if (ls[midpoint] == item)
    return true;
  else if (item < ls[midpoint]) 
    return binary_search_r (ls, first, midpoint - 1, item);
  else 
    return binary_search_r (ls, midpoint + 1, last, item);
}

bool binary_search_i (int ls[], int length, int item) {
  int first = 0;
  int last = length - 1;
  bool found = false;
  
  while (!found && first <= last) {
    int midpoint = (first + last) / 2;
    if (ls[midpoint] == item)
      found = true;
    else if (item < ls[midpoint])
      last = midpoint - 1;
    else 
      first = midpoint + 1;
  }
  return found;
}

int main() {
  int ls []  = {1, 2, 4, 5, 9};
  int length = 5;
  cout << "Item list: ";
  for (int i = 0; i < length; i++) {
    cout << ls[i] << " ";;
  }
  cout << "\n";
  cout << "Item to look for: ";
  int item;
  cin >> item;
  
  cout << "0 for recursive; 1 for iteratve: ";
  int choice;
  cin >> choice;
  
  if (choice == 0) {
    if (binary_search_r (ls, 0, length, item))
      cout << "Item found.\n";
    else
      cout << "Item not found.\n";
  }
  else {
    if (binary_search_i (ls, length, item))
      cout << "Item found.\n";
    else
      cout << "Item not found.\n";
  }
  return 0;
}
