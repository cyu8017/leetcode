// LeetCode 3961 - Maximize Sum of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/


class Solution {
    func maxRatings(_ units: [[Int]]) -> Int {
        let n = units[0].count
        if n == 1 {
            var ans = 0
            for x in units { ans += x[0] }
            return ans
        }
        var answer = 0
        var mn = Int.max, mn2 = Int.max
        for x in units {
            var x = x.sorted()
            answer += x[1]
            mn2 = min(mn2, x[1])
            mn = min(mn, x[0])
        }
        return answer - (mn2 - mn)
    }
}
