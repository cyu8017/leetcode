// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution {
    func maxFrequencyElements(_ nums: [Int]) -> Int {
        var cnt = Array(repeating: 0, count: 101)
        for x in nums { cnt[x] += 1 }
        var mx = -1, ans = 0
        for x in cnt {
            if mx < x {
                mx = x
                ans = x
            } else if mx == x {
                ans += x
            }
        }
        return ans
    }
}
