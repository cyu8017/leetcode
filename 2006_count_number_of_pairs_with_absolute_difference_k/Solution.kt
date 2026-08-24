// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution {
    fun countKDifference(nums: IntArray, k: Int): Int {
var freq: HashMap<Int, Int> = HashMap()
var ans: Int = 0
for (x in nums) {
ans += freq.getOrDefault(x - k, 0)
ans += freq.getOrDefault(x + k, 0)
freq.merge(x, 1, { a, b -> a + b })
}
return ans
}
}
