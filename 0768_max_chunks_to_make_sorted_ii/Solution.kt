// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

class Solution {
    fun maxChunksToSorted(arr: IntArray): Int {
        var n = arr.size
        var maxLeft = IntArray(n)
        var minRight = IntArray(n)
        maxLeft[0] = arr[0]
        for (i in 1 until n) { maxLeft[i] = maxOf(maxLeft[i - 1], arr[i]) }
        minRight[n - 1] = arr[n - 1]
        run {
            var i = n - 2
            while (i >= 0) {
                minRight[i] = minOf(minRight[i + 1], arr[i])
                i--
            }
        }
        var chunks = 1
        for (i in 0 until n - 1) { if (maxLeft[i] <= minRight[i + 1]) chunks++ }
        return chunks
    }
}
