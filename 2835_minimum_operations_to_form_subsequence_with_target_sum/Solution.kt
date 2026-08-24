// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

class Solution {
    fun minOperations(nums: IntArray, target: Int): Int {
        var cnt = IntArray(32)
        var sum = 0
        for (v in nums) {
            sum += v
            var b = 0
            while ((1  shl  b) < v) b++
            cnt[b]++
        }
        if (sum < target) return -1
        var ans = 0
        for (i in 0 until 31) {
            if ((target & (1  shl  i)) != 0) {
                if (cnt[i] > 0) cnt[i]--
                else {
                    var j = i + 1
                    while (j < 32 && cnt[j] == 0) j++
                    if (j == 32) return -1
                    while (j > i) {
                        cnt[j]--
                        cnt[j - 1] += 2
                        ans++
                        j--
                    }
                    cnt[i]--
                }
            }
            cnt[i + 1] += cnt[i] / 2
        }
        return ans
    }
}
