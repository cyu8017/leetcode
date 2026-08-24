// LeetCode 0991 - Broken Calculator
// https://leetcode.com/problems/broken-calculator/

class Solution {
    fun brokenCalc(startValue: Int, target: Int): Int {
var ans: Int = 0
while (target > startValue) {
if (target % 2 == 1) {
target++
}
else {
target /= 2
}
ans++
}
return ans + startValue - target
}
}
