// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

class Solution {
    func minReverseOperations(_ n: Int, _ p: Int, _ banned: [Int], _ k: Int) -> [Int] {
        let ban = Set(banned)
        var ans = [Int](repeating: -1, count: n)
        ans[p] = 0
        var next0 = Array(0...n)
        var next1 = Array(0...n)
        func find(_ next: inout [Int], _ x: Int) -> Int {
            if next[x] != x {
                next[x] = find(&next, next[x])
            }
            return next[x]
        }
        func remove(_ x: Int) {
            if x % 2 == 0 {
                next0[x] = find(&next0, x + 2 <= n ? x + 2 : n)
            } else {
                next1[x] = find(&next1, x + 2 <= n ? x + 2 : n)
            }
        }
        for b in banned { remove(b) }
        remove(p)
        var q = [p]
        var qi = 0
        while qi < q.count {
            let i = q[qi]; qi += 1
            let lo = max(i - (k - 1), 0)
            let hi = min(i, n - k)
            if lo > hi { continue }
            let minJ = lo + (lo + k - 1) - i
            let maxJ = hi + (hi + k - 1) - i
            let start = max(0, minJ)
            let end = min(n - 1, maxJ)
            if start > end { continue }
            if (i + k - 1) % 2 == 0 {
                var x = find(&next0, start % 2 == 0 ? start : start + 1)
                while x <= end {
                    if !ban.contains(x) && ans[x] == -1 {
                        ans[x] = ans[i] + 1
                        q.append(x)
                        remove(x)
                    }
                    x = find(&next0, x + 2 <= n ? x + 2 : n)
                }
            } else {
                var x = find(&next1, start % 2 == 1 ? start : start + 1)
                while x <= end {
                    if !ban.contains(x) && ans[x] == -1 {
                        ans[x] = ans[i] + 1
                        q.append(x)
                        remove(x)
                    }
                    x = find(&next1, x + 2 <= n ? x + 2 : n)
                }
            }
        }
        return ans
    }
}
