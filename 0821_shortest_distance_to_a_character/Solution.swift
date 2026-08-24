// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution {
    func shortestToChar(_ s: String, _ c: Character) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var ans = Array(repeating: 0, count: n)
        var prev = -n
        for i in 0..<n {
            if chars[i] == c { prev = i }
            ans[i] = i - prev
        }
        prev = 2 * n
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == c { prev = i }
            ans[i] = min(ans[i], prev - i)
        }
        return ans
    }
}
