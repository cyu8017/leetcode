// LeetCode 2176 - Count Equal and Divisible Pairs in an Array
// https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution {
    fun countPairs(nums: IntArray, k: Int): Int {
        var ans: Int = 0
        for (i in 0 until nums.size)
            for (j in i + 1 until nums.size)
                if (nums[i] == nums[j] && (i * j) % k == 0) ans++
        return ans
    }
}
