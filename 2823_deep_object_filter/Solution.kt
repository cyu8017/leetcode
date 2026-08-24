// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/
// JS-only problem; Java vector filter stand-in.

class Solution {
    fun deepFilter(obj: IntArray, fn: IntPredicate): MutableList<Int> {
        var output = ArrayList<Int>()
        for (v in obj) { if (fn.test(v)) output.add(v) }
        return output
    }
}
