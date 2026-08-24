// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

class Solution {
    fun minimumSum(n: Int, k: Int): Int {
        var used = HashSet<Int>()
        var sum = 0
        var x = 1
        while (used.size < n) {
            if (!used.contains(k - x)) {
                used.add(x)
                sum += x
            }
            x++
        }
        return sum
    }
}
