// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

class Solution {
    fun stableMountains(height: IntArray, threshold: Int): MutableList<Int> {
        var ans = ArrayList<Int>()
        for (i in 1 until height.size) {
            if (height[i - 1] > threshold) ans.add(i)
        }
        return ans
    }
}
