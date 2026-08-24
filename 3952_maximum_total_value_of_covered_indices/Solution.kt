// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

class Solution {
    fun maxTotalValue(nums: IntArray, s: String): Int {
        var answer = 0
        var i = 0
        while (i < s.length) {
            if (s[i] == '0') { i++; continue }
            val start = i
            while (i < s.length && s[i] == '1') i++
            val end = i - 1
            if (start == 0) {
                for (index in start..end) answer += nums[index]
                continue
            }
            var minimum = nums[start - 1]
            var total = 0
            for (index in (start - 1)..end) {
                total += nums[index]
                if (nums[index] < minimum) minimum = nums[index]
            }
            answer += total - minimum
        }
        return answer
    }
}
