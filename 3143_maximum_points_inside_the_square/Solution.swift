// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

class Solution {
    func maxPointsInsideSquare(_ points: [[Int]], _ s: String) -> Int {
        let chars = Array(s)
        var g: [Int: [Int]] = [:]
        for i in 0..<points.count {
            let key = max(abs(points[i][0]), abs(points[i][1]))
            g[key, default: []].append(i)
        }
        var vis = Array(repeating: false, count: 26)
        var ans = 0
        let a = Character("a").asciiValue!
        for key in g.keys.sorted() {
            for i in g[key]! {
                let j = Int(chars[i].asciiValue! - a)
                if vis[j] { return ans }
                vis[j] = true
            }
            ans += g[key]!.count
        }
        return ans
    }
}
