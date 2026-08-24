// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

class Solution {
    func maxConsecutive(_ bottom: Int, _ top: Int, _ special: [Int]) -> Int {
        let special = special.sorted()
        var ans = special[0] - bottom
        for i in 1..<special.count {
            ans = max(ans, special[i] - special[i - 1] - 1)
        }
        ans = max(ans, top - special[special.count - 1])
        return ans
    }
}
