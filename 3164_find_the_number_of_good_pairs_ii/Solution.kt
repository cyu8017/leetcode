// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, k: Int): Long {
        var cnt1 = HashMap<Int, Int>()
        for (x in nums1) { if (x % k == 0) cnt1.merge(x / k, 1, Integer::sum) }
        if (cnt1.isEmpty()) return 0
        var cnt2 = HashMap<Int, Int>()
        for (x in nums2) { cnt2.merge(x, 1, Integer::sum) }
        var mx = 0
        for (x in cnt1.keys) { mx = maxOf(mx, x) }
        var ans = 0
        for (e in cnt2) {
            var x = e.key, v = e.value
            var s = 0
            var y = x
            while (y <= mx) {
                var c = cnt1[y]
                if (c != null) s += c
                y += x
            }
            ans += s * v
        }
        return ans
    }
}
