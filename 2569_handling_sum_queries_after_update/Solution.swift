// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

class Solution {
    func handleQuery(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums1.count
        var ones = [Int](repeating: 0, count: 4 * n)
        var lazy = [Bool](repeating: false, count: 4 * n)
        func build(_ idx: Int, _ l: Int, _ r: Int) {
            if l == r {
                ones[idx] = nums1[l]
                return
            }
            let m = (l + r) / 2
            build(idx * 2, l, m)
            build(idx * 2 + 1, m + 1, r)
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]
        }
        func apply(_ idx: Int, _ l: Int, _ r: Int) {
            ones[idx] = (r - l + 1) - ones[idx]
            lazy[idx].toggle()
        }
        func push(_ idx: Int, _ l: Int, _ r: Int) {
            if lazy[idx] && l != r {
                let m = (l + r) / 2
                apply(idx * 2, l, m)
                apply(idx * 2 + 1, m + 1, r)
                lazy[idx] = false
            }
        }
        func update(_ idx: Int, _ l: Int, _ r: Int, _ ql: Int, _ qr: Int) {
            if ql <= l && r <= qr {
                apply(idx, l, r)
                return
            }
            push(idx, l, r)
            let m = (l + r) / 2
            if ql <= m { update(idx * 2, l, m, ql, qr) }
            if qr > m { update(idx * 2 + 1, m + 1, r, ql, qr) }
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]
        }
        build(1, 0, n - 1)
        var sum2 = nums2.reduce(0, +)
        var ans = [Int]()
        for q in queries {
            if q[0] == 1 { update(1, 0, n - 1, q[1], q[2]) }
            else if q[0] == 2 { sum2 += q[1] * ones[1] }
            else { ans.append(sum2) }
        }
        return ans
    }
}
