// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

class Solution {
    fun partitionArray(nums: IntArray, k: Int): Boolean {
        val n = nums.size
        if (n % k != 0) return false
        val m = n / k
        var mx = 0
        for (x in nums) mx = maxOf(mx, x)
        val cnt = IntArray(mx + 1)
        for (x in nums) {
            cnt[x]++
            if (cnt[x] > m) return false
        }
        return true
    }
}
