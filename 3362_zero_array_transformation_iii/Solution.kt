// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

class Solution {
    fun maxRemoval(nums: IntArray, queries: Array<IntArray>): Int {
        queries.sortWith { a, b -> a[0].compareTo(b[0]) }
        var h = PriorityQueue(compareByDescending { it })
        var n = nums.size
        var diff = IntArray(n + 1)
        var j = 0
        var used = 0
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            while (j < queries.size && queries[j][0] == i) {
                h.offer(queries[j][1])
                j++
            }
            while (cur < nums[i]) {
                if (h.isEmpty() || h.peek() < i) return -1
                var r = h.poll()
                cur++
                diff[r + 1] = diff[r + 1] - 1
                used++
            }
        }
        return queries.size - used
    }
}
