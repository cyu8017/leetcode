// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution {
    func earliestFullBloom(_ plantTime: [Int], _ growTime: [Int]) -> Int {
        let idx = plantTime.indices.sorted { growTime[$0] > growTime[$1] }
        var day = 0, ans = 0
        for i in idx {
            day += plantTime[i]
            ans = max(ans, day + growTime[i])
        }
        return ans
    }
}
