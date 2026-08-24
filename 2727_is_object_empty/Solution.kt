// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

class Solution {
    fun isEmpty(obj: MutableMap<String, Int>): Boolean {
        return obj.size == 0
    }

    fun isEmpty(arr: IntArray): Boolean {
        return arr.size == 0
    }
}
