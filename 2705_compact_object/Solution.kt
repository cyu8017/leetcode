// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

class Solution {
    fun compactObject(obj: IntArray): IntArray {
        val out = ArrayList<Int>()
        for (x in obj) if (x != 0) out.add(x)
        return out.toIntArray()
    }
}
