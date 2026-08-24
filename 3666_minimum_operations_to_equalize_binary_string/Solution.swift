// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

class Solution {
    func minOperations(_ s: String, _ k: Int) -> Int {
        let n = s.count
        var ts = [Set<Int>(), Set<Int>()]
        for i in 0...n { ts[i % 2].insert(i) }
        var cnt0 = 0
        for c in s where c == "0" { cnt0 += 1 }
        ts[cnt0 % 2].remove(cnt0)
        var q = [cnt0]
        var ans = 0
        while !q.isEmpty {
            var nq = [Int]()
            for cur in q {
                if cur == 0 { return ans }
                let l = cur + k - 2 * min(cur, k)
                let r = cur + k - 2 * max(k - n + cur, 0)
                var t = ts[l % 2]
                var it = t.filter { $0 >= l && $0 <= r }
                for v in it {
                    nq.append(v)
                    t.remove(v)
                }
                ts[l % 2] = t
            }
            q = nq
            ans += 1
        }
        return -1
    }
}
