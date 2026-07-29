// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution {
    func numPairsDivisibleBy60(_ time: [Int]) -> Int {
        var count = Array(repeating: 0, count: 60)
        var ans = 0
        for t in time {
            ans += count[(60 - t % 60) % 60]
            count[t % 60] += 1
        }
        return ans
    }
}
