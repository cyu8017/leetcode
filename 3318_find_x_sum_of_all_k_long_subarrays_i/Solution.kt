// LeetCode 3318 - Find X-Sum of All K-Long Subarrays I
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

class Solution {
    fun findXSum(nums: IntArray, k: Int, x: Int): IntArray {
        val n = nums.size
        val ans = IntArray(n - k + 1)
        for (i in 0..n - k) {
            val freq = HashMap<Int, Int>()
            for (j in i until i + k) freq[nums[j]] = (freq[nums[j]] ?: 0) + 1
            val arr = ArrayList<IntArray>()
            for ((key, value) in freq) arr.add(intArrayOf(key, value))
            for (a in arr.indices) {
                for (b in a + 1 until arr.size) {
                    val A = arr[a]
                    val B = arr[b]
                    if (B[1] > A[1] || (B[1] == A[1] && B[0] > A[0])) {
                        arr[a] = B
                        arr[b] = A
                    }
                }
            }
            val lim = minOf(x, arr.size)
            val keep = HashSet<Int>()
            for (t in 0 until lim) keep.add(arr[t][0])
            var sum = 0
            for (j in i until i + k) if (nums[j] in keep) sum += nums[j]
            ans[i] = sum
        }
        return ans
    }
}
