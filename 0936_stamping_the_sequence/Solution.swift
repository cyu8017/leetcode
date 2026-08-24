// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

class Solution {
    func movesToStamp(_ stamp: String, _ target: String) -> [Int] {
        let stamp = Array(stamp), target = Array(target)
        let n = target.count, m = stamp.count
        var done = Array(repeating: false, count: n)
        var ans = [Int]()
        var changed = true
        while changed {
            changed = false
            if n >= m {
                for i in stride(from: n - m, through: 0, by: -1) {
                    var ok = true, any = false
                    for j in 0..<m {
                        if !done[i + j] && target[i + j] != stamp[j] { ok = false; break }
                        if !done[i + j] { any = true }
                    }
                    if ok && any {
                        for j in 0..<m { done[i + j] = true }
                        ans.append(i)
                        changed = true
                        break
                    }
                }
            }
        }
        if done.contains(false) { return [] }
        return ans.reversed()
    }
}
