// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

class Solution {
    fun minSwaps(nums: IntArray, forbidden: IntArray): Int {
        var n = nums.size
        var freq = HashMap<Int, Int>()
        for (x in nums) {
            if (!freq.containsKey(x)) freq[x] = 0
            freq[x] = freq.getOrDefault(x, 0) + 1
        }
        for (x in forbidden) {
            if (!freq.containsKey(x)) freq[x] = 0
            freq[x] = freq.getOrDefault(x, 0) + 1
        }
        for (c in freq.values) {
            if (c > n) return -1
        }
        var bad = HashMap<Int, Int>()
        var total = 0
        var largest = 0
        for (i in 0 until n) {
            if (nums[i] == forbidden[i]) {
                if (!bad.containsKey(nums[i])) bad[nums[i]] = 0
                bad[nums[i]] = bad.getOrDefault(nums[i], 0) + 1
                total = total + 1
                if (bad[nums[i]] > largest) largest = bad[nums[i]]
            }
        }
        if ((total + 1) / 2 > largest) return (total + 1) / 2
        return largest
    }
}
