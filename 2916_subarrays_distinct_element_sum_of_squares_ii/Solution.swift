// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

class Solution {
    private let mod = 1_000_000_007
    private var tree: [Node] = []

    private class Node {
        var sum = 0
        var sumSq = 0
        var lazy = 0
    }

    func sumCounts(_ nums: [Int]) -> Int {
        let n = nums.count
        var last: [Int: Int] = [:]
        tree = (0..<(4 * (n + 2))).map { _ in Node() }
        var ans = 0
        for i in 1...n {
            let v = nums[i - 1]
            let prev = last[v, default: 0]
            update(1, 1, n, prev + 1, i, 1)
            ans = (ans + tree[1].sumSq) % mod
            last[v] = i
        }
        return ans
    }

    private func apply(_ idx: Int, _ l: Int, _ r: Int, _ val: Int) {
        let length = r - l + 1
        tree[idx].sumSq = (tree[idx].sumSq + 2 * val % mod * tree[idx].sum % mod
            + val % mod * val % mod * length % mod) % mod
        tree[idx].sum = (tree[idx].sum + val % mod * length % mod) % mod
        tree[idx].lazy = (tree[idx].lazy + val) % mod
    }

    private func update(_ idx: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int, _ val: Int) {
        if ql > r || qr < l { return }
        if ql <= l && r <= qr {
            apply(idx, l, r, val)
            return
        }
        if tree[idx].lazy != 0 && l != r {
            let mid = (l + r) / 2
            apply(idx * 2, l, mid, tree[idx].lazy)
            apply(idx * 2 + 1, mid + 1, r, tree[idx].lazy)
            tree[idx].lazy = 0
        }
        let mid = (l + r) / 2
        update(idx * 2, l, mid, ql, qr, val)
        update(idx * 2 + 1, mid + 1, r, ql, qr, val)
        tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % mod
        tree[idx].sumSq = (tree[idx * 2].sumSq + tree[idx * 2 + 1].sumSq) % mod
    }
}
