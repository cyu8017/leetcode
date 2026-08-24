// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

class Solution {
    fun minimumMoves(nums: IntArray, k: Int, maxChanges: Int): Long {
        var n = nums.size
        var cnt = IntArray(n + 1), s = IntArray(n + 1)
        for (i in 1 until = n) {
            cnt[i] = cnt[i - 1] + nums[i - 1]
            s[i] = s[i - 1] + i * nums[i - 1]
        }
        var ans = Long.MAX_VALUE
        for (i in 1 until = n) {
            var t = 0
            var need = k - nums[i - 1]
            for (j in intArrayOf(i - 1, i + 1)) {
                if (need > 0 && 1 <= j && j <= n && nums[j - 1] == 1) {
                    need--
                    t++
                }
            }
            var c = minOf(need, maxChanges)
            need -= c
            t += c * 2L
            if (need <= 0) {
                ans = minOf(ans, t)
                continue
            }
            var l = 2, r = maxOf(i - 1, n - i)
            while (l <= r) {
                var mid = (l + r)  shr  1
                var l1 = maxOf(1, i - mid), r1 = maxOf(0, i - 2)
                var l2 = minOf(n + 1, i + 2), r2 = minOf(n, i + mid)
                var c1 = cnt[r1] - cnt[l1 - 1]
                var c2 = cnt[r2] - cnt[l2 - 1]
                if (c1 + c2 >= need) {
                    var t1 = c1 * i - (s[r1] - s[l1 - 1])
                    var t2 = s[r2] - s[l2 - 1] - c2 * i
                    ans = minOf(ans, t + t1 + t2)
                    r = mid - 1
                } else {
                    l = mid + 1
                }
            }
        }
        return ans
    }
}
