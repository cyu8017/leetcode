// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

class Solution {
    func maxIncreasingGroups(_ usageLimits: [Int]) -> Int {
        let arr = usageLimits.sorted()
        var ans = 0, sum = 0
        for v in arr {
            sum += v
            let need = (ans + 1) * (ans + 2) / 2
            if sum >= need { ans += 1 }
        }
        return ans
    }
}
