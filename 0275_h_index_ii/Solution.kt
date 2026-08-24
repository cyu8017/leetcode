// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

class Solution {
    fun hIndex(citations: IntArray): Int {
        var left = 0
        var right = citations.size - 1
        val length = citations.size
        while (left <= right) {
            val mid = (left + right) / 2
            val papers = length - mid
            if (citations[mid] >= papers) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return length - left
    }
}
