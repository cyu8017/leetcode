// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution {
    func maxLength(_ arr: [String]) -> Int {
        var masks: [(Int, Int)] = []
        for s in arr {
            var mask = 0
            var ok = true
            for ch in s {
                let bit = 1 << Int(ch.asciiValue! - Character("a").asciiValue!)
                if mask & bit != 0 { ok = false; break }
                mask |= bit
            }
            if ok { masks.append((mask, s.count)) }
        }
        var ans = 0
        func dfs(_ i: Int, _ mask: Int, _ len: Int) {
            ans = max(ans, len)
            for j in i..<masks.count {
                if mask & masks[j].0 == 0 {
                    dfs(j + 1, mask | masks[j].0, len + masks[j].1)
                }
            }
        }
        dfs(0, 0, 0)
        return ans
    }
}
