// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution {
    fun maxOperations(nums: IntArray, k: Int): Int {
        val c = HashMap<Int, Int>()
        var ans = 0
        for (x in nums) {
            val need = k - x
            val avail = c[need] ?: 0
            if (avail > 0) {
                c[need] = avail - 1
                ans++
            } else {
                c[x] = (c[x] ?: 0) + 1
            }
        }
        return ans
    }
}
