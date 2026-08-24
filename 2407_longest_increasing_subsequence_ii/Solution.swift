// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

class Solution {
    func lengthOfLIS(_ nums: [Int], _ k: Int) -> Int {
        let maxV = nums.max() ?? 0
        var tree = [Int](repeating: 0, count: 4 * (maxV + 1))
        func update(_ idx: Int, _ l: Int, _ r: Int, _ pos: Int, _ val: Int) {
            if l == r {
                tree[idx] = max(tree[idx], val)
                return
            }
            let mid = (l + r) / 2
            if pos <= mid { update(idx * 2, l, mid, pos, val) }
            else { update(idx * 2 + 1, mid + 1, r, pos, val) }
            tree[idx] = max(tree[idx * 2], tree[idx * 2 + 1])
        }
        func query(_ idx: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) -> Int {
            if qr < l || r < ql { return 0 }
            if ql <= l && r <= qr { return tree[idx] }
            let mid = (l + r) / 2
            return max(query(idx * 2, l, mid, ql, qr), query(idx * 2 + 1, mid + 1, r, ql, qr))
        }
        var ans = 0
        for x in nums {
            let lo = max(1, x - k)
            var best = 1
            if lo <= x - 1 { best = query(1, 1, maxV, lo, x - 1) + 1 }
            update(1, 1, maxV, x, best)
            ans = max(ans, best)
        }
        return ans
    }
}
