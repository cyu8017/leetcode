// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution {
    func maxDistance(_ colors: [Int]) -> Int {
        let n = colors.count
        var ans = 0
        for i in 0..<n {
            if colors[i] != colors[0] { ans = max(ans, i) }
            if colors[i] != colors[n - 1] { ans = max(ans, n - 1 - i) }
        }
        return ans
    }
}
