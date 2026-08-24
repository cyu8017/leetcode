// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

class Solution {
    fun findMaxSum(nums1: IntArray, nums2: IntArray, k: Int): LongArray {
        val n = nums1.size
        val arr = Array(n) { i -> intArrayOf(nums1[i], nums2[i], i) }
        arr.sortBy { it[0] }
        val ans = LongArray(n)
        val h = PriorityQueue<Int>()
        var sum = 0L
        var i = 0
        while (i < n) {
            val v = arr[i][0]
            val start = i
            while (i < n && arr[i][0] == v) i++
            for (t in start until i) ans[arr[t][2]] = sum
            for (t in start until i) {
                h.offer(arr[t][1])
                sum += arr[t][1].toLong()
                if (h.size > k) sum -= h.poll().toLong()
            }
        }
        return ans
    }
}
