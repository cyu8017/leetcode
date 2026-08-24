// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution {
    private var nums: IntArray? = null
    private var buckets: IntArray? = null
    private var target: Int = 0

    private fun dfs(index: Int): Boolean {
        if (index == nums.size) return true
        for (i in 0 until buckets.size) {
            if (buckets[i] + nums[index] > target) continue
            buckets[i] += nums[index]
            if (dfs(index + 1)) return true
            buckets[i] -= nums[index]
            if (buckets[i] == 0) break
        }
        return false
    }

    fun canPartitionKSubsets(nums: IntArray, k: Int): Boolean {
        var total = 0
        for (x in nums) { total += x }
        if (total % k != 0) return false
        target = total / k
        this.nums = nums.clone()
        this.nums.sort()
        var i = 0
        var j = this.nums.size - 1
        while (i < j) {
            var tmp = this.nums[i]
            this.nums[i] = this.nums[j]
            this.nums[j] = tmp
            i++, j--
        }
        if (this.nums[0] > target) return false
        buckets = IntArray(k)
        return dfs(0)
    }
}
