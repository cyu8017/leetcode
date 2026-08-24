// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

private class Node {
    var l = 0, r = 0
    var s00 = 0, s01 = 0, s10 = 0, s11 = 0
}

class Solution {
    private var tr: [Node] = []

    func maximumSumSubsequence(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let n = nums.count
        tr = (0..<(n * 4)).map { _ in Node() }
        build(1, 1, n)
        for i in 0..<n { modify(1, i + 1, nums[i]) }
        let MOD = 1_000_000_007
        var ans = 0
        for q in queries {
            modify(1, q[0] + 1, q[1])
            ans = (ans + query(1, 1, n)) % MOD
        }
        return ans
    }

    private func build(_ u: Int, _ l: Int, _ r: Int) {
        tr[u].l = l
        tr[u].r = r
        if l == r { return }
        let mid = (l + r) >> 1
        build(u << 1, l, mid)
        build(u << 1 | 1, mid + 1, r)
    }

    private func pushup(_ u: Int) {
        let left = tr[u << 1], right = tr[u << 1 | 1]
        tr[u].s00 = max(left.s00 + right.s10, left.s01 + right.s00)
        tr[u].s01 = max(left.s00 + right.s11, left.s01 + right.s01)
        tr[u].s10 = max(left.s10 + right.s10, left.s11 + right.s00)
        tr[u].s11 = max(left.s10 + right.s11, left.s11 + right.s01)
    }

    private func modify(_ u: Int, _ x: Int, _ v: Int) {
        if tr[u].l == tr[u].r {
            tr[u].s11 = max(0, v)
            return
        }
        let mid = (tr[u].l + tr[u].r) >> 1
        if x <= mid { modify(u << 1, x, v) }
        else { modify(u << 1 | 1, x, v) }
        pushup(u)
    }

    private func query(_ u: Int, _ l: Int, _ r: Int) -> Int {
        if tr[u].l >= l && tr[u].r <= r { return tr[u].s11 }
        let mid = (tr[u].l + tr[u].r) >> 1
        var ans = 0
        if r <= mid { ans = query(u << 1, l, r) }
        if l > mid { ans = max(ans, query(u << 1 | 1, l, r)) }
        return ans
    }
}
