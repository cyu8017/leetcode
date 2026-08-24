// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

class Solution {
    func numberOfNodes(_ n: Int, _ queries: [Int]) -> Int {
        var flip = [Int](repeating: 0, count: n + 1)
        var val = [Int](repeating: 0, count: n + 1)
        for q in queries { flip[q] ^= 1 }
        var ans = 0
        for i in 1...n {
            val[i] = flip[i]
            if i > 1 { val[i] ^= val[i / 2] }
            ans += val[i]
        }
        return ans
    }
}
