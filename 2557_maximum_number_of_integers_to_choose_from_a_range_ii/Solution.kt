// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

class Solution {
    private var ans: Int = 0
    private var remain: Long = 0L

    fun maxCount(banned: IntArray, n: Int, maxSum: Long): Int {
        banned.sort()
        var uniq = ArrayList<Int>()
        for (x in banned) {
            if (x >= 1 && x <= n && (uniq.isEmpty() || uniq[uniq.size - 1] != x)) uniq.add(x)
        }
        ans = 0
        remain = maxSum
        var prev = 0
        for (b in uniq) {
            check(prev + 1L, b - 1L)
            prev = b
        }
        check(prev + 1L, n)
        return ans
    }

    private fun check(l: Long, r: Long) {
        if (l > r || remain <= 0) return
        var lo = l
        var hi = r
        var best = l - 1
        while (lo <= hi) {
            var mid = (lo + hi) / 2
            var cnt = mid - l + 1
            var sum = (l + mid) * cnt / 2
            if (sum <= remain) {
                best = mid
                lo = mid + 1
            } else hi = mid - 1
        }
        if (best >= l) {
            var cnt = (best - l + 1)
            ans += cnt
            remain -= (l + best) * cnt / 2
        }
    }
}
