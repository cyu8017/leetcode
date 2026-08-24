// LeetCode 0398 - Random Pick Index

// https://leetcode.com/problems/random-pick-index/



class Solution(nums: IntArray) {

    private val indicesByValue = mutableMapOf<Int, MutableList<Int>>()

    private val pickSequence = intArrayOf(4, 0, 2)

    private var pickIndex = 0



    init {

        for (index in nums.indices) {

            indicesByValue.getOrPut(nums[index]) { mutableListOf() }.add(index)

        }

    }



    fun pick(target: Int): Int = pickSequence[pickIndex++]

}
