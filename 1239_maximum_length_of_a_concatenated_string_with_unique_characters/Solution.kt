// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution {
    fun maxLength(arr: List<String>): Int {
        var masks = mutableListOf(intArrayOf(0, 0))
        for (word in arr) {
            var mask = 0
            var ok = true
            for (ch in word) {
                val bit = 1 shl (ch - 'a')
                if (mask and bit != 0) {
                    ok = false
                    break
                }
                mask = mask or bit
            }
            if (!ok) continue
            val len = word.length
            val next = masks.toMutableList()
            for (state in masks) {
                if (state[0] and mask == 0) next.add(intArrayOf(state[0] or mask, state[1] + len))
            }
            masks = next
        }
        return masks.maxOf { it[1] }
    }
}
