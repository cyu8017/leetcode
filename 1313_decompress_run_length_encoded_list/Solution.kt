// LeetCode 1313 - Decompress Run-Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution {
    fun decompressRLElist(nums: IntArray): IntArray {
        val answer = mutableListOf<Int>()
        var i = 0
        while (i < nums.size) {
            repeat(nums[i]) { answer.add(nums[i + 1]) }
            i += 2
        }
        return answer.toIntArray()
    }
}
