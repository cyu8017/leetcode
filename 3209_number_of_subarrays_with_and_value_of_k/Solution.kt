// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

class Solution {
    fun countSubarrays(nums: IntArray, k: Int): Long {
        var pre = HashMap<Int, Int>()
        var ans = 0
        for (x in nums) {
            var cur = HashMap<Int, Int>()
            for (Map.Entry<Integer, Integer> kv : pre.entrySet()) {
                cur.merge(x & kv.getKey(), kv.getValue(), Integer::sum)
            }
            cur.merge(x, 1, Integer::sum)
            ans += cur.getOrDefault(k, 0)
            pre = cur
        }
        return ans
    }
}
