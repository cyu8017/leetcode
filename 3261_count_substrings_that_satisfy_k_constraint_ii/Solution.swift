// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

class Solution {
    func countKConstraintSubstrings(_ s: String, _ k: Int, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var leftMost = Array(repeating: 0, count: n)
        var z = 0, o = 0, L = 0
        for R in 0..<n {
            if chars[R] == "0" { z += 1 } else { o += 1 }
            while z > k && o > k {
                if chars[L] == "0" { z -= 1 } else { o -= 1 }
                L += 1
            }
            leftMost[R] = L
        }
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + (i - leftMost[i] + 1) }
        return queries.map { q in
            let l = q[0], r = q[1]
            var lo = l, hi = r + 1
            while lo < hi {
                let mid = (lo + hi) / 2
                if leftMost[mid] < l { lo = mid + 1 }
                else { hi = mid }
            }
            var res = 0
            if lo > l {
                let m = lo - l
                res += m * (m + 1) / 2
            }
            if lo <= r { res += pref[r + 1] - pref[lo] }
            return res
        }
    }
}
