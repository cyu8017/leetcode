// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution {

    fun maximumBags(capacity: IntArray, rocks: IntArray, additionalRocks: Int): Int {

            var need = IntArray(capacity.size)
            for (i in 0 until capacity.size) { need[i] = capacity[i] - rocks[i] }
            need.sort()
            var ans = 0
            for (n in need) {
                if (additionalRocks < n) break
                additionalRocks -= n
                ans++
            }
            return ans

    }

}
