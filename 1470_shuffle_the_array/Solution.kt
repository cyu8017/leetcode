// LeetCode 1470 - Shuffle the Array
// https://leetcode.com/problems/shuffle-the-array/

class Solution {
    fun shuffle(nums: IntArray, n: Int): IntArray {
        val answer = IntArray(2 * n)
        for (i in 0 until n) {
            answer[2 * i] = nums[i]
            answer[2 * i + 1] = nums[i + n]
        }
        return answer
    }
}
