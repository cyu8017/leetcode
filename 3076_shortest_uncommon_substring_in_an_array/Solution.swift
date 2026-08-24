// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

class Solution {
    func shortestSubstrings(_ arr: [String]) -> [String] {
        let n = arr.count
        var ans = Array(repeating: "", count: n)
        for i in 0..<n {
            let s = Array(arr[i])
            let m = s.count
            var j = 1
            while j <= m && ans[i].isEmpty {
                for l in 0...(m - j) {
                    let sub = String(s[l..<(l + j)])
                    if ans[i].isEmpty || ans[i] > sub {
                        var ok = true
                        for k in 0..<n {
                            if k != i && arr[k].contains(sub) {
                                ok = false
                                break
                            }
                        }
                        if ok { ans[i] = sub }
                    }
                }
                j += 1
            }
        }
        return ans
    }
}
