// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

class Solution {
    func minLength(_ s: String, _ numOps: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var lo = 1, hi = n
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(chars, n, numOps, mid) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ s: [Character], _ n: Int, _ numOps: Int, _ L: Int) -> Bool {
        if L == 0 { return false }
        var ops = 0
        var i = 0
        while i < n {
            var j = i
            while j < n && s[j] == s[i] { j += 1 }
            ops += (j - i) / (L + 1)
            i = j
        }
        return ops <= numOps
    }
}
