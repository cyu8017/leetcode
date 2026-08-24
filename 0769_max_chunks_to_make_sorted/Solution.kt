// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution {
    fun maxChunksToSorted(arr: IntArray): Int {
        var chunks = 0
        var maxSoFar = 0
        for (i in 0 until arr.size) {
            maxSoFar = maxOf(maxSoFar, arr[i])
            if (maxSoFar == i) chunks++
        }
        return chunks
    }
}
