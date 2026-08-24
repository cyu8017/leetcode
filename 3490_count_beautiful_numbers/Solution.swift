// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

class Solution {
    func beautifulNumbers(_ l: Int, _ r: Int) -> Int {
        return countBeautiful(r) - countBeautiful(l - 1)
    }

    private func countBeautiful(_ n: Int) -> Int {
        if n <= 0 { return 0 }
        let s = Array(String(n))
        func dfs(_ pos: Int, _ tight: Bool, _ sum: Int, _ prod: Int, _ started: Bool) -> Int {
            if pos == s.count {
                if !started { return 0 }
                return (sum > 0 && prod % sum == 0) ? 1 : 0
            }
            let up = tight ? Int(s[pos].asciiValue! - 48) : 9
            var ans = 0
            for d in 0...up {
                let nt = tight && d == up
                if !started && d == 0 { ans += dfs(pos + 1, nt, 0, 1, false) }
                else {
                    let ns = sum + d
                    let np = !started ? d : prod * d
                    ans += dfs(pos + 1, nt, ns, np, true)
                }
            }
            return ans
        }
        return dfs(0, true, 0, 1, false)
    }
}
