// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

class Solution {
    fun minimalKSum(nums: IntArray, k: Int): Long {
        nums.sort()
        var ans: Long = 0
        var prev: Int = 0
        for (x in nums) {
            if (x <= prev) continue
            var start: Int = prev + 1, end = x - 1
            if (start <= end) {
                var cnt: Int = end - start + 1
                if (cnt > k) { end = start + k - 1; cnt = k; }
                ans += (start + end).toLong() * cnt / 2
                k -= cnt
                if (k == 0) return ans
            }
            prev = x
        }
        var s: Long = prev + 1, e = s + k - 1
        ans += (s + e) * k / 2
        return ans
    }
}
