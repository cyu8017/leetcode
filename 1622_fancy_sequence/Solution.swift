// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

class Fancy {
    private let MOD = 1_000_000_007
    private var n = 0
    private let size = 1 << 17
    private var tree: [Int]
    private var mul: [Int]
    private var add: [Int]

    init() {
        tree = [Int](repeating: 0, count: 2 * size)
        mul = [Int](repeating: 1, count: 2 * size)
        add = [Int](repeating: 0, count: 2 * size)
    }

    private func apply(_ p: Int, _ m: Int, _ a: Int) {
        tree[p] = Int((Int64(tree[p]) * Int64(m) + Int64(a)) % Int64(MOD))
        mul[p] = Int((Int64(mul[p]) * Int64(m)) % Int64(MOD))
        add[p] = Int((Int64(add[p]) * Int64(m) + Int64(a)) % Int64(MOD))
    }

    private func push(_ p: Int) {
        if mul[p] != 1 || add[p] != 0 {
            apply(2 * p, mul[p], add[p])
            apply(2 * p + 1, mul[p], add[p])
            mul[p] = 1
            add[p] = 0
        }
    }

    private func update(_ p: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int, _ m: Int, _ a: Int) {
        if ql <= l && r <= qr {
            apply(p, m, a)
            return
        }
        push(p)
        let mid = (l + r) / 2
        if ql <= mid { update(2 * p, l, mid, ql, qr, m, a) }
        if qr > mid { update(2 * p + 1, mid + 1, r, ql, qr, m, a) }
    }

    private func get(_ p: Int, _ l: Int, _ r: Int, _ i: Int) -> Int {
        if l == r { return tree[p] }
        push(p)
        let mid = (l + r) / 2
        return i <= mid ? get(2 * p, l, mid, i) : get(2 * p + 1, mid + 1, r, i)
    }

    func append(_ val: Int) {
        update(1, 0, size - 1, n, n, 0, val % MOD)
        n += 1
    }

    func addAll(_ inc: Int) {
        if n > 0 { update(1, 0, size - 1, 0, n - 1, 1, inc % MOD) }
    }

    func multAll(_ m: Int) {
        if n > 0 { update(1, 0, size - 1, 0, n - 1, m % MOD, 0) }
    }

    func getIndex(_ idx: Int) -> Int {
        idx < n ? get(1, 0, size - 1, idx) : -1
    }
}
