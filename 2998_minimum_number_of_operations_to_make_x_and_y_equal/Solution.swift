// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

class Solution {
    func minimumOperationsToMakeEqual(_ x: Int, _ y: Int) -> Int {
        if x <= y { return y - x }
        var q = [(x, 0)]
        var seen: Set<Int> = [x]
        var head = 0
        while head < q.count {
            let (v, d) = q[head]
            head += 1
            if v == y { return d }
            var cands = [v + 1, v - 1]
            if v % 11 == 0 { cands.append(v / 11) }
            if v % 5 == 0 { cands.append(v / 5) }
            for nxt in cands where nxt > 0 && nxt < 2 * x + 20 && seen.insert(nxt).inserted {
                q.append((nxt, d + 1))
            }
        }
        return -1
    }
}
