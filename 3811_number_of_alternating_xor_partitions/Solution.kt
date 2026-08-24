// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number_of_alternating_xor_partitions/

class Solution {
    fun alternatingXOR(nums: IntArray, target1: Int, target2: Int): Int {
        val MOD = 1_000_000_007
        val cnt1 = HashMap<Int, Int>()
        val cnt2 = HashMap<Int, Int>()
        cnt2[0] = 1
        var pre = 0
        var ans = 0
        for (x in nums) {
            pre = pre xor x
            val a = cnt2.getOrDefault(pre xor target1, 0)
            val b = cnt1.getOrDefault(pre xor target2, 0)
            ans = (a + b) % MOD
            cnt1[pre] = (cnt1.getOrDefault(pre, 0) + a) % MOD
            cnt2[pre] = (cnt2.getOrDefault(pre, 0) + b) % MOD
        }
        return ans
    }
}
