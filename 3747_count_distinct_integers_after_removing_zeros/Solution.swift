// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

class Solution {
    private var s = [Character]()
    private var m = 0
    private var f = [[[[Int]]]]()

    func countDistinct(_ n: Int) -> Int {
        s = Array(String(n))
        m = s.count
        f = Array(repeating: Array(repeating: Array(repeating: [Int](repeating: -1, count: 2), count: 2), count: 2), count: 20)
        return dfs(0, 0, 1, 1)
    }

    private func dfs(_ i: Int, _ zero: Int, _ lead: Int, _ limit: Int) -> Int {
        if i == m { return (zero == 0 && lead == 0) ? 1 : 0 }
        if limit == 0 && f[i][zero][lead][limit] != -1 { return f[i][zero][lead][limit] }
        let up = limit == 1 ? Int(s[i].asciiValue! - 48) : 9
        var ans = 0
        for d in 0...up {
            var nxtZero = zero
            if d == 0 && lead == 0 { nxtZero = 1 }
            let nxtLead = (lead == 1 && d == 0) ? 1 : 0
            let nxtLimit = (limit == 1 && d == up) ? 1 : 0
            ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit)
        }
        if limit == 0 { f[i][zero][lead][limit] = ans }
        return ans
    }
}
