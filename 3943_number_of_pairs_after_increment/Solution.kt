// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, queries: Array<IntArray>): LongArray {
        val blockSize = 225
        val n = nums2.size
        val blocks = (n + blockSize - 1) / blockSize
        val lazy = IntArray(blocks)
        val freq = Array(blocks) { HashMap<Int, Int>() }
        for (b in 0 until blocks) rebuild(freq, nums2, b, blockSize, n)
        val fixed = HashMap<Int, Int>()
        for (x in nums1) fixed[x] = fixed.getOrDefault(x, 0) + 1
        val answer = ArrayList<Long>()
        for (q in queries) {
            if (q[0] == 1) {
                val l = q[1]
                val r = q[2]
                val delta = q[3]
                val first = l / blockSize
                val last = r / blockSize
                if (first == last) {
                    push(lazy, nums2, first, blockSize, n)
                    for (i in l..r) nums2[i] += delta
                    rebuild(freq, nums2, first, blockSize, n)
                    continue
                }
                push(lazy, nums2, first, blockSize, n)
                for (i in l until (first + 1) * blockSize) nums2[i] += delta
                rebuild(freq, nums2, first, blockSize, n)
                push(lazy, nums2, last, blockSize, n)
                for (i in last * blockSize..r) nums2[i] += delta
                rebuild(freq, nums2, last, blockSize, n)
                for (b in first + 1 until last) lazy[b] += delta
            } else {
                var total = 0L
                for ((a, countA) in fixed) {
                    val target = q[1] - a
                    for (b in 0 until blocks) {
                        val c = freq[b][target - lazy[b]]
                        if (c != null) total += countA.toLong() * c
                    }
                }
                answer.add(total)
            }
        }
        return answer.toLongArray()
    }

    private fun rebuild(freq: Array<HashMap<Int, Int>>, nums2: IntArray, b: Int, blockSize: Int, n: Int) {
        freq[b].clear()
        val end = minOf((b + 1) * blockSize, n)
        for (i in b * blockSize until end) freq[b][nums2[i]] = freq[b].getOrDefault(nums2[i], 0) + 1
    }

    private fun push(lazy: IntArray, nums2: IntArray, b: Int, blockSize: Int, n: Int) {
        if (lazy[b] != 0) {
            val end = minOf((b + 1) * blockSize, n)
            for (i in b * blockSize until end) nums2[i] += lazy[b]
            lazy[b] = 0
        }
    }
}
