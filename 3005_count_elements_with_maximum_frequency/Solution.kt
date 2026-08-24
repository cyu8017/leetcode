// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution {
    fun maxFrequencyElements(nums: IntArray): Int {
        var cnt = IntArray(101)
        for (x in nums) { cnt[x]++ }
        var mx = -1
        var ans = 0
        for (x in cnt) {
            if (mx < x) {
                mx = x
                ans = x
            } else if (mx == x) {
                ans += x
            }
        }
        return ans
    }
}
