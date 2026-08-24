// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

class Solution {
    private var chars: [Character] = []
    private var k = 0
    private var n = 0
    private var memo: [Int: Int] = [:]

    func maxPartitionsAfterOperations(_ s: String, _ k: Int) -> Int {
        chars = Array(s)
        self.k = k
        n = chars.count
        memo = [:]
        return dfs(0, 0, 1)
    }

    private func dfs(_ i: Int, _ cur: Int, _ t: Int) -> Int {
        if i >= n { return 1 }
        let kkey = (i << 32) | (cur << 1) | t
        if let v = memo[kkey] { return v }
        let aVal = Int(Character("a").asciiValue!)
        let v = 1 << (Int(chars[i].asciiValue!) - aVal)
        var nxt = cur | v
        var ans: Int
        if nxt.nonzeroBitCount > k {
            ans = dfs(i + 1, v, t) + 1
        } else {
            ans = dfs(i + 1, nxt, t)
        }
        if t > 0 {
            for j in 0..<26 {
                nxt = cur | (1 << j)
                if nxt.nonzeroBitCount > k {
                    ans = max(ans, dfs(i + 1, 1 << j, 0) + 1)
                } else {
                    ans = max(ans, dfs(i + 1, nxt, 0))
                }
            }
        }
        memo[kkey] = ans
        return ans
    }
}
