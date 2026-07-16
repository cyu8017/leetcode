// LeetCode 0201 - Bitwise AND of Numbers Range\n// https://leetcode.com/problems/\n\nclass Solution {
    fun rangeBitwiseAnd(left: Int, right: Int): Int {
        var low = left; var high = right; var shift = 0
        while (low < high) { low = low shr 1; high = high shr 1; shift++ }
        return low shl shift
    }
}
