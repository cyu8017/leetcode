// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

class Solution {
    func maxRemovals(_ source: String, _ pattern: String, _ targetIndices: [Int]) -> Int {
        let s = Array(source), p = Array(pattern)
        let n = s.count
        var lo = 0, hi = targetIndices.count
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(mid, s, p, targetIndices, n) { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }

    private func ok(_ removeFirst: Int, _ s: [Character], _ p: [Character], _ targetIndices: [Int], _ n: Int) -> Bool {
        var mark = Array(repeating: false, count: n)
        for i in 0..<removeFirst { mark[targetIndices[i]] = true }
        var j = 0
        for i in 0..<n where j < p.count {
            if mark[i] { continue }
            if s[i] == p[j] { j += 1 }
        }
        return j == p.count
    }
}
