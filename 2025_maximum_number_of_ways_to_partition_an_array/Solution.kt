// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

class Solution {
    fun waysToPartition(nums: IntArray, k: Int): Int {
var n: Int = nums.size
var pref: LongArray = LongArray(n)
pref[0] = nums[0]
for (i in 1 until n) {
pref[i] = pref[i - 1] + nums[i]
}
var total: Long = pref[n - 1]
var right: HashMap<Long, Int> = HashMap()
var left: HashMap<Long, Int> = HashMap()
for (i in 0 until n - 1) {
right.merge(pref[i], 1, { a, b -> a + b })
}
var ans: Int = 0
if (total % 2 == 0) {
ans = right.getOrDefault(total / 2, 0)
}
for (i in 0 until n) {
var diff: Long = k.toLong() - nums[i]
var newTotal: Long = total + diff
var cur: Int = 0
if (newTotal % 2 == 0) {
var half: Long = newTotal / 2
cur = left.getOrDefault(half, 0) + right.getOrDefault(half - diff, 0)
}
ans = maxOf(ans, cur)
if (i < n - 1) {
left.merge(pref[i], 1, { a, b -> a + b })
right.put(pref[i], right[pref[i]] - 1)
}
}
return ans
}
}
