# DataStructures_P2
The following is a series of projects completed as part of Udacity Nanodegree program in Data Structures and Algorithms. It focuses on algorithms

AutocompletewithTries:

TrieNode contains children and is_word members and insert and suffixes methods. The time complexity for the insert is O(1)

The suffixes methods recursively calls itself on each node and counts all complete words under itself
Time Complexity is O(N) is where N total length of nodes under the trieNode, not just immediate children but the children of its children too.
Space Complexity is O(N) where N total length of nodes under the trieNode

Trie contains an element which is a TrieNode and contains insert and find methods.

Insert method inserts word for the trie by creating several trie nodes until every character is iterated.
Time Complexity is O(N) for insert operation is where N is the length of the word
Space Complexity is O(N) since N trieNodes and characters are used.

The Find method returns a trieNode for the specific prefix
Time Complexity and Space Complexity is O(N) where N is the total number of nodes in the Trie.


DutchNationalFlag:

Navigated through the list in single traversal without using another data structure but using two variables for zero and two indices used for the sort.

zero_index is initialized with a value of 0 whereas two_index is initialized with the last element of the array. We ignore all elements with one and only address zeros and twos for swapping.

If the element is two, insert two at two_index and decrement it. As a sub-case of the value at the two_index is two, just continue by decrementing the two_index
If the value at the two_index is one, just swap it.
If it is zero, insert zero at the zero_index, and increment the zero_index by 1 and replace the current element value with the zero index element.

If the value is zero, just swap it with the value at the zero_index

Time Complexity is O(N) where N is the length of the array
Space Complexity is O(N), because we used so many memory locations for the operation

MaxMinUnsorted:

Uses two variables one for max and min, both initialized with the first element of the array.
Check if those need to be replaced when navigating across the list depending on value.
If the min value is greater than any element of the array, we replace the min value with the lower value and proceed to the next element.
Similarly, if the max value is lower than the current element we replace the max value.

Time Complexity is O(N) where N is the length of the array. Completed in single traversal.
Space Complexity is O(N), because we used so many memory locations for the iteration.


RearrangeArrayDigits:

The basic idea is to use merge sort logic until the last step. In the last step defined by array bounds, we can instead choose the largest number and create a list of two array elements. 

I used recursive implementation of merge sort because that is the most intuitive one.

Time Complexity is O(NLogN) where N is the length of the array
Space Complexity is O(N) too. Though we used a helper array, it is of the same size of the original array.


RotatedSortedArray:

Since the array is pivoted, there is at least one half of the array which is sorted. Using this idea, follow the steps.

Step1) split array into two 
Step2) check for the bounds in each two and identify which one is the sorted or unsorted array'
Step3) if the target is within bounds of the sorted array, just split it in two and search for it using the first, last and the middle elements
Step4) if the target is within unsorted, repeat'

Since the array is split into two each time, until we maintain time complexity to O(logn)
Space Complexity is O(N) because we keep working on use two variable min and max and keep updating them until we get the result


RouterTrie:

RouteTrieNode contains two members children to hold the word/RouteTrieNode combo and handler which is a message used to for relevant leaf nodes. It contains an insert function makes an entry into the RouteTrieNode combo. Time Complexity and space complexity for the function is O(1)

RouterTrie contains a root element which is a RouteTrieNode type and two methods insert and find as outlined by the boilerplate code. 

Insert navigates through each path outlined by the list of words and calls the insert function on the RouteTrieNode to create nodes wherever necessary. On the last word of the list, it updates the handler message to message specified. Worst Case time Complexity is O(N) where N is the length of words. Worst Case Space Complexity is O(N*K) where K is the length of the largest word

Find recursively navigates through the children of the root and looks for the first word If it does not match it returns None. If it does, it calls recursively to find the next word within that node and continues until it finds the last node. Worst case time Complexity is O(N*M) where N is the length of words and M is the total nodes in the Trie. Space Complexity is O(N*M*K) where K is the length of the largest word.

Router contains the routertrie and performs add_handler and lookup operations after splitting the nodes on "/" character. 

The Time Complexity for add_handler is the the same as "insert" on the RouterTrie + O(N) to account for split_path operation where N is the length of the path . Space Complexity is O(N) too.

The Time Complexity for lookup is the the same as "find" on the RouterTrie + O(N) to account for split_path operation where N is the length of the path. Space Complexity is O(N) too.


SquareRootInteger:

Initiate the range for the square root defined by min and max values to 1 and the number itself.
Keep updating the range and assign the min value when the range cannot be further reduced or the number equals to the product.
To maintain time complexity O(logn) I keep on dividing the max value by 2 and min value to (max+min)//2

Time Complexity is O(logn) because we divide the range by half each time
Space Compexity is O(1) because we keep working on use two variable min and max and keep updating them until we get the result
