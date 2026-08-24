// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

class Solution {
    fun minOperations(nums: IntArray): Int {
var n: Int = nums.size
var uniq: IntArray = Arrays.stream(nums).distinct().sorted().toArray()
var ans: Int = n
var j: Int = 0
for (i in 0 until uniq.size) {
while (j < uniq.size && uniq[j] - uniq[i] + 1 <= n) {
j++
}
ans = minOf(ans, n - (j - i))
}
return ans
}
}
