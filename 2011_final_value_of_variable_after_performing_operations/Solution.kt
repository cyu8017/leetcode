// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution {
    fun finalValueAfterOperations(operations: Array<String>): Int {
var x: Int = 0
for (op in operations) {
if (op[1] == '+') {
x++
}
else {
x--
}
}
return x
}
}
