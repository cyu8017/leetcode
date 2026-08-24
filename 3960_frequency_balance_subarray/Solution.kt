// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

class Solution {
    fun getLength(nums: IntArray): Int {
        var n = nums.size
        var ans = 1
        for (l in 0 until n) {
            var cnt = HashMap<Int, Int>()
            var freq = HashMap<Int, Int>()
            for (r in l until n) {
                var x = nums[r]
                var c = cnt.getOrDefault(x, 0)
                if (freq.getOrDefault(c, 0) > 0) {
                    var fc = freq[c] - 1
                    if (fc == 0) freq.remove(c)
                    else freq[c] = fc
                }
                cnt[x] = c + 1
                freq[cnt[x]] = freq.getOrDefault(cnt[x], 0 + 1)
                var cx = cnt[x]
                if (cnt.size == 1 || (freq.size == 2 && (freq.getOrDefault(cx * 2, 0) > 0 || (cx % 2 == 0 && freq.getOrDefault(cx / 2, 0) > 0)))) {
                    ans = maxOf(ans, r - l + 1)
                }
            }
        }
        return ans
    }
}
