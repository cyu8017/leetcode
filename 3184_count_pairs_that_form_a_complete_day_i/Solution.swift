// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution {
    func countCompleteDayPairs(_ hours: [Int]) -> Int {
        var cnt = Array(repeating: 0, count: 24)
        var ans = 0
        for x in hours {
            ans += cnt[(24 - x % 24) % 24]
            cnt[x % 24] += 1
        }
        return ans
    }
}
