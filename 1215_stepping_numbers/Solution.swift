// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

class Solution {
    func countSteppingNumbers(_ low: Int, _ high: Int) -> [Int] {
        var ans: [Int] = []
        if low == 0 { ans.append(0) }
        var q = Array(1...9)
        var qi = 0
        while qi < q.count {
            let cur = q[qi]; qi += 1
            if cur > high { continue }
            if cur >= low { ans.append(cur) }
            let last = cur % 10
            if last > 0 {
                let nxt = cur * 10 + last - 1
                if nxt <= high { q.append(nxt) }
            }
            if last < 9 {
                let nxt = cur * 10 + last + 1
                if nxt <= high { q.append(nxt) }
            }
        }
        return ans
    }
}
