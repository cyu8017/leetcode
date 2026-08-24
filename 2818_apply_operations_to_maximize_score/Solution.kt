// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

class Solution {
    private val MOD = 1_000_000_007

    fun maximumScore(nums: MutableList<Int>, k: Int): Int {
        val n = nums.size
        var maxV = 0
        for (v in nums) maxV = maxOf(maxV, v)
        val spf = IntArray(maxV + 1)
        for (i in 2..maxV) {
            if (spf[i] == 0) {
                var j = i
                while (j <= maxV) {
                    if (spf[j] == 0) spf[j] = i
                    j += i
                }
            }
        }
        val score = IntArray(n)
        for (i in 0 until n) score[i] = primeScore(nums[i], spf)
        val left = IntArray(n)
        val right = IntArray(n)
        val st = ArrayList<Int>()
        for (i in 0 until n) {
            while (st.isNotEmpty() && score[st[st.size - 1]] < score[i]) st.removeAt(st.size - 1)
            left[i] = if (st.isEmpty()) -1 else st[st.size - 1]
            st.add(i)
        }
        st.clear()
        for (i in n - 1 downTo 0) {
            while (st.isNotEmpty() && score[st[st.size - 1]] <= score[i]) st.removeAt(st.size - 1)
            right[i] = if (st.isEmpty()) n else st[st.size - 1]
            st.add(i)
        }
        val arr = Array(n) { LongArray(2) }
        for (i in 0 until n) {
            arr[i][0] = nums[i].toLong()
            arr[i][1] = 1L * (i - left[i]) * (right[i] - i)
        }
        arr.sortWith(compareByDescending { it[0] })
        var ans = 1L
        var remain = k.toLong()
        for (pair in arr) {
            if (remain <= 0) break
            val use = minOf(pair[1], remain)
            ans = ans * modPow(pair[0], use) % MOD
            remain -= use
        }
        return ans.toInt()
    }

    private fun primeScore(x0: Int, spf: IntArray): Int {
        var x = x0
        val seen = HashSet<Int>()
        while (x > 1) {
            val p = spf[x]
            seen.add(p)
            while (x % p == 0) x /= p
        }
        return seen.size
    }

    private fun modPow(a0: Long, b0: Long): Long {
        var a = a0 % MOD
        var b = b0
        var res = 1L
        while (b > 0) {
            if ((b and 1L) != 0L) res = res * a % MOD
            a = a * a % MOD
            b = b shr 1
        }
        return res
    }
}
