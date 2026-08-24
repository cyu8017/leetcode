// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

class Solution {
    private class Node {
        var l = 0, r = 0, mn = 0, mx = 0, lazy = 0
    }

    private class SegmentTree {
        var tr: [Node]
        init(_ n: Int) {
            tr = (0..<(n << 2)).map { _ in Node() }
            build(1, 0, n)
        }
        func build(_ u: Int, _ l: Int, _ r: Int) {
            tr[u].l = l; tr[u].r = r; tr[u].mn = 0; tr[u].mx = 0; tr[u].lazy = 0
            if l == r { return }
            let mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)
        }
        func apply(_ u: Int, _ v: Int) {
            tr[u].mn += v
            tr[u].mx += v
            tr[u].lazy += v
        }
        func pushup(_ u: Int) {
            tr[u].mn = min(tr[u << 1].mn, tr[u << 1 | 1].mn)
            tr[u].mx = max(tr[u << 1].mx, tr[u << 1 | 1].mx)
        }
        func pushdown(_ u: Int) {
            if tr[u].lazy != 0 {
                let v = tr[u].lazy
                apply(u << 1, v)
                apply(u << 1 | 1, v)
                tr[u].lazy = 0
            }
        }
        func modify(_ u: Int, _ l: Int, _ r: Int, _ v: Int) {
            if tr[u].l >= l && tr[u].r <= r {
                apply(u, v)
                return
            }
            pushdown(u)
            let mid = (tr[u].l + tr[u].r) >> 1
            if l <= mid { modify(u << 1, l, r, v) }
            if r > mid { modify(u << 1 | 1, l, r, v) }
            pushup(u)
        }
        func query(_ u: Int, _ target: Int) -> Int {
            if tr[u].l == tr[u].r { return tr[u].l }
            pushdown(u)
            let left = u << 1, right = u << 1 | 1
            if tr[left].mn <= target && target <= tr[left].mx { return query(left, target) }
            return query(right, target)
        }
    }

    func longestBalanced(_ nums: [Int]) -> Int {
        let n = nums.count
        let st = SegmentTree(n)
        var last = [Int: Int]()
        var now = 0, ans = 0
        for i in 1...n {
            let x = nums[i - 1]
            let det = (x & 1) != 0 ? 1 : -1
            if let prev = last[x] {
                st.modify(1, prev, n, -det)
                now -= det
            }
            last[x] = i
            st.modify(1, i, n, det)
            now += det
            let pos = st.query(1, now)
            ans = max(ans, i - pos)
        }
        return ans
    }
}
