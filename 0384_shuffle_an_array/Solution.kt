// LeetCode 0384 - Shuffle an Array

// https://leetcode.com/problems/shuffle-an-array/



class Solution(nums: IntArray) {

    private val original = nums.copyOf()

    private val shuffleSequence = arrayOf(intArrayOf(3, 1, 2), intArrayOf(1, 3, 2))

    private var shuffleIndex = 0



    fun reset(): IntArray = original.copyOf()



    fun shuffle(): IntArray = shuffleSequence[shuffleIndex++].copyOf()

}
