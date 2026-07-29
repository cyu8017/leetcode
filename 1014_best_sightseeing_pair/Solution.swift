// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

class Solution {
    func maxScoreSightseeingPair(_ values: [Int]) -> Int {
        var best = values[0]
        var ans = 0
        for j in 1..<values.count {
            ans = max(ans, best + values[j] - j)
            best = max(best, values[j] + j)
        }
        return ans
    }
}
