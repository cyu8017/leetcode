// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

class Solution {
    fun firstUniqueFreq(nums: IntArray): Int {
        var cnt = HashMap<Int, Int>()
        for (x in nums) { cnt[x] = cnt.getOrDefault(x, 0 + 1) }
        var freq = HashMap<Int, Int>()
        for (v in cnt.values) { freq[v] = freq.getOrDefault(v, 0 + 1) }
        for (x in nums) {
            if (freq[cnt[x]] == 1) return x
        }
        return -1
    }
}
