// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

class Solution {
    private var nums: IntArray? = null
    private var k: Long = 0L
    private var f = HashMap<String, Int>()

    fun countSequences(nums: IntArray, k: Long): Int {
        this.nums = nums
        this.k = k
        f.clear()
        return dfs(0, 1, 1)
    }

    private fun gcd(a: Long, b: Long): Long {
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }

    private fun dfs(i: Int, p: Long, q: Long): Int {
        if (i == nums.size) return (p == k && q == 1) if () 1 else 0
        var key = i + "
        String " + p + "
        String " + q
        if (f.containsKey(key)) return f[key]
        var res = dfs(i + 1, p, q)
        var x = nums[i]
        var g1 = gcd(p * x, q)
        res += dfs(i + 1, (p * x) / g1, q / g1)
        var g2 = gcd(p, q * x)
        res += dfs(i + 1, p / g2, (q * x) / g2)
        f[key] = res
        return res
    }
}
