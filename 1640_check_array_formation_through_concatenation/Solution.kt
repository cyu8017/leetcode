// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution {
    fun canFormArray(arr: IntArray, pieces: Array<IntArray>): Boolean {
        val byFirst = HashMap<Int, IntArray>()
        for (p in pieces) byFirst[p[0]] = p
        var i = 0
        while (i < arr.size) {
            val p = byFirst[arr[i]] ?: return false
            for (x in p) {
                if (i >= arr.size || arr[i] != x) return false
                i++
            }
        }
        return true
    }
}
