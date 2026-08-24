// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

class Solution {
    fun pourWater(heights: IntArray, volume: Int, k: Int): IntArray {
        for (v in 0 until volume) {
            var index = k
            for (i in k - 1 downTo 0) {
                if (heights[i] > heights[index]) break
                if (heights[i] < heights[index]) index = i
            }
            if (index != k) { heights[index]++; continue; }
            index = k
            for (i in k + 1 until heights.size) {
                if (heights[i] > heights[index]) break
                if (heights[i] < heights[index]) index = i
            }
            heights[index]++
        }
        return heights
    }
}
