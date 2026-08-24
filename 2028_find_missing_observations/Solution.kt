// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

class Solution {
    fun missingRolls(rolls: IntArray, mean: Int, n: Int): IntArray {
var sum: Int = 0
for (r in rolls) {
sum += r
}
var remain: Int = mean * (rolls.size + n) - sum
if (remain < n || remain > 6 * n) {
return IntArray(0)
}
var ans: IntArray = IntArray(n)
var baseVal: Int = remain / n
var extra: Int = remain % n
for (i in 0 until n) {
ans[i] = baseVal + (if (i < extra) 1 else 0)
}
return ans
}
}
