// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution {
    fun kItemsWithMaximumSum(numOnes: Int, numZeros: Int, numNegOnes: Int, k: Int): Int {
        var remain = k
        var ans = 0
        var take = minOf(numOnes, remain)
        ans += take
        remain -= take
        take = minOf(numZeros, remain)
        remain -= take
        take = minOf(numNegOnes, remain)
        ans -= take
        return ans
    }
}
