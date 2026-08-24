// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

class Solution {
    func countInterestingSubarrays(_ nums: [Int], _ modulo: Int, _ k: Int) -> Int {
        var freq: [Int: Int] = [0: 1]
        var ans = 0
        var pref = 0
        for v in nums {
            if v % modulo == k { pref += 1 }
            var need = (pref - k) % modulo
            if need < 0 { need += modulo }
            ans += freq[need, default: 0]
            freq[pref % modulo, default: 0] += 1
        }
        return ans
    }
}
