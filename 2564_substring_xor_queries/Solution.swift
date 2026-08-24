// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

class Solution {
    func substringXorQueries(_ s: String, _ queries: [[Int]]) -> [[Int]] {
        let chars = Array(s)
        let n = chars.count
        var pos = [Int: [Int]]()
        for i in 0..<n {
            if chars[i] == "0" {
                if pos[0] == nil { pos[0] = [i, i] }
                continue
            }
            var val = 0
            var j = i
            while j < n && j < i + 30 {
                val = val * 2 + Int(chars[j].asciiValue! - Character("0").asciiValue!)
                if pos[val] == nil { pos[val] = [i, j] }
                j += 1
            }
        }
        return queries.map { pos[$0[0] ^ $0[1]] ?? [-1, -1] }
    }
}
