// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

class Solution {
    fun relocateMarbles(nums: IntArray, moveFrom: IntArray, moveTo: IntArray): MutableList<Int> {
        val pos = HashSet<Int>()
        for (x in nums) pos.add(x)
        for (i in moveFrom.indices) {
            pos.remove(moveFrom[i])
            pos.add(moveTo[i])
        }
        return pos.sorted().toMutableList()
    }
}
