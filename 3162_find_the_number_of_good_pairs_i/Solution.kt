// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, k: Int): Int {
        var ans = 0
        for (x in nums1)
            for (y in nums2)
                if (x % (y * k) == 0) ans++
        return ans
    }
}
