// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution {
    fun missingMultiple(nums: IntArray, k: Int): Int {
        val s = HashSet<Int>()
        for (x in nums) s.add(x)
        var i = 1
        while (true) {
            val x = k * i
            if (x !in s) return x
            i++
        }
    }
}
