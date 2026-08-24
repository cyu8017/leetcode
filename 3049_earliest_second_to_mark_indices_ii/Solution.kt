// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

class Solution {
    private fun getSecondToIndex(nums: IntArray, changeIndices: IntArray): MutableMap<Int, Int> {
        var indexToFirstSecond = HashMap<Int, Int>()
        for (second in 0 until changeIndices.size) {
            var index = changeIndices[second] - 1
            if (nums[index] > 0 && !indexToFirstSecond.containsKey(index))
                indexToFirstSecond[index] = second
        }
        var secondToIndex = HashMap<Int, Int>()
        for (e in indexToFirstSecond)
            secondToIndex[e.value] = e.key
        return secondToIndex
    }

    private fun canMark(nums: IntArray, secondToIndex: MutableMap<Int, Int>, maxSecond: Int, numsSum: Long): Boolean {
        var h = PriorityQueue<Int>()
        var marks = 0
        for (second in maxSecond - 1 downTo 0) {
            if (secondToIndex.containsKey(second)) {
                h.offer(nums[secondToIndex[second]])
                if (marks == 0) {
                    h.poll()
                    marks++
                } else {
                    marks--
                }
            } else {
                marks++
            }
        }
        var heapSize = h.size
        var heapSum = 0
        while (!h.isEmpty()) heapSum += h.poll()
        var decrementAndMarkCost = numsSum - heapSum + (nums.size - heapSize)
        var zeroAndMarkCost = heapSize + heapSize
        return decrementAndMarkCost + zeroAndMarkCost <= maxSecond
    }

    fun earliestSecondToMarkIndices(nums: IntArray, changeIndices: IntArray): Int {
        var secondToIndex = getSecondToIndex(nums, changeIndices)
        var numsSum = 0
        for (v in nums) { numsSum += v }
        var l = 0
        var r = changeIndices.size + 1
        while (l < r) {
            var m = (l + r) / 2
            if (canMark(nums, secondToIndex, m, numsSum)) r = m
            else l = m + 1
        }
        return if (l <= changeIndices.size) l else -1
    }
}
