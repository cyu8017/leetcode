// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

class Solution {
    func meetRequirement(_ n: Int, _ lights: [[Int]], _ requirement: [Int]) -> Int {
        var diff = [Int](repeating: 0, count: n + 1)
        for light in lights {
            let pos = light[0], r = light[1]
            let l = max(0, pos - r)
            let rr = min(n - 1, pos + r)
            diff[l] += 1
            diff[rr + 1] -= 1
        }
        var ans = 0, cur = 0
        for i in 0..<n {
            cur += diff[i]
            if cur >= requirement[i] { ans += 1 }
        }
        return ans
    }
}
