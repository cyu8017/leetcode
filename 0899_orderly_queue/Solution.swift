// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

class Solution {
    func orderlyQueue(_ s: String, _ k: Int) -> String {
        if k > 1 { return String(s.sorted()) }
        var best = s
        let doubled = s + s
        let chars = Array(doubled)
        let n = s.count
        for i in 1..<n {
            let cand = String(chars[i..<(i + n)])
            if cand < best { best = cand }
        }
        return best
    }
}
