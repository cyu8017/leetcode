// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution {
    func executeInstructions(_ n: Int, _ startPos: [Int], _ s: String) -> [Int] {
        let chars = Array(s)
        let m = chars.count
        var ans = [Int](repeating: 0, count: m)
        for i in 0..<m {
            var r = startPos[0], c = startPos[1], cnt = 0
            for j in i..<m {
                let ch = chars[j]
                if ch == "L" { c -= 1 }
                else if ch == "R" { c += 1 }
                else if ch == "U" { r -= 1 }
                else { r += 1 }
                if r < 0 || r >= n || c < 0 || c >= n { break }
                cnt += 1
            }
            ans[i] = cnt
        }
        return ans
    }
}
