// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

class Solution {
    func distinctPoints(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var f = Array(repeating: 0, count: n + 1)
        var g = Array(repeating: 0, count: n + 1)
        var x = 0, y = 0
        for i in 1...n {
            let c = chars[i - 1]
            if c == "U" { y += 1 }
            else if c == "D" { y -= 1 }
            else if c == "L" { x -= 1 }
            else { x += 1 }
            f[i] = x
            g[i] = y
        }
        var st = Set<String>()
        if k <= n {
            for i in k...n {
                let a = f[n] - (f[i] - f[i - k])
                let b = g[n] - (g[i] - g[i - k])
                st.insert("\(a),\(b)")
            }
        }
        return st.count
    }
}
