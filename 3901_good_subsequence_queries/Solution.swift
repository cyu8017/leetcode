// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

class Solution {
    private class Node {
        var l = 0, r = 0, g = 0
    }

    private class SegmentTree {
        var tr: [Node]
        init(_ n: Int) {
            tr = (0..<(n << 2)).map { _ in Node() }
            build(1, 1, n)
        }
        func build(_ u: Int, _ l: Int, _ r: Int) {
            tr[u].l = l; tr[u].r = r; tr[u].g = 0
            if l == r { return }
            let mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)
        }
        func pushup(_ u: Int) { tr[u].g = gcd(tr[u << 1].g, tr[u << 1 | 1].g) }
        func modify(_ u: Int, _ x: Int, _ v: Int) {
            if tr[u].l == tr[u].r { tr[u].g = v; return }
            let mid = (tr[u].l + tr[u].r) >> 1
            if x <= mid { modify(u << 1, x, v) }
            else { modify(u << 1 | 1, x, v) }
            pushup(u)
        }
        func query(_ u: Int, _ l: Int, _ r: Int) -> Int {
            if l > r { return 0 }
            if tr[u].l >= l && tr[u].r <= r { return tr[u].g }
            let mid = (tr[u].l + tr[u].r) >> 1
            if r <= mid { return query(u << 1, l, r) }
            if l > mid { return query(u << 1 | 1, l, r) }
            return gcd(query(u << 1, l, mid), query(u << 1 | 1, mid + 1, r))
        }
        static func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        func gcd(_ a: Int, _ b: Int) -> Int { SegmentTree.gcd(a, b) }
    }

    func countGoodSubseq(_ nums: [Int], _ p: Int, _ queries: [[Int]]) -> Int {
        var nums = nums
        let n = nums.count
        let tree = SegmentTree(n)
        var cnt = 0
        for i in 0..<n {
            if nums[i] % p == 0 {
                tree.modify(1, i + 1, nums[i])
                cnt += 1
            }
        }
        var ans = 0
        for q in queries {
            let idx = q[0], val = q[1]
            if nums[idx] % p == 0 {
                tree.modify(1, idx + 1, 0)
                cnt -= 1
            }
            if val % p == 0 {
                tree.modify(1, idx + 1, val)
                cnt += 1
            }
            nums[idx] = val
            if tree.tr[1].g != p { continue }
            if cnt < n || n > 6 {
                ans += 1
                continue
            }
            for i in 1...n {
                let leftG = tree.query(1, 1, i - 1)
                let rightG = tree.query(1, i + 1, n)
                var g = leftG, b = rightG
                while b != 0 { let t = g % b; g = b; b = t }
                if g == p { ans += 1; break }
            }
        }
        return ans
    }
}
