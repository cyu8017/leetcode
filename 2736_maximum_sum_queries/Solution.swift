// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

class Solution {
    func maximumSumQueries(_ nums1: [Int], _ nums2: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums1.count
        var pts = (0..<n).map { [nums1[$0], nums2[$0], nums1[$0] + nums2[$0]] }
        pts.sort { $0[0] > $1[0] }
        var qs = queries.enumerated().map { i, q in [q[0], q[1], i] }
        qs.sort { $0[0] > $1[0] }
        var ys = nums2 + queries.map { $0[1] }
        ys.sort()
        var uniq: [Int] = []
        for y in ys {
            if uniq.isEmpty || uniq.last != y { uniq.append(y) }
        }
        let m = uniq.count
        var bit = Array(repeating: -1, count: m + 2)
        var ans = Array(repeating: 0, count: queries.count)
        var j = 0
        for q in qs {
            while j < n && pts[j][0] >= q[0] {
                update(&bit, m, m - rank(uniq, pts[j][1]) + 1, pts[j][2])
                j += 1
            }
            ans[q[2]] = query(bit, m - rank(uniq, q[1]) + 1)
        }
        return ans
    }

    private func rank(_ ys: [Int], _ y: Int) -> Int {
        var lo = 0, hi = ys.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if ys[mid] < y { lo = mid + 1 } else { hi = mid }
        }
        return lo + 1
    }

    private func update(_ bit: inout [Int], _ m: Int, _ i0: Int, _ v: Int) {
        var i = i0
        while i <= m {
            bit[i] = max(bit[i], v)
            i += i & -i
        }
    }

    private func query(_ bit: [Int], _ i0: Int) -> Int {
        var i = i0, best = -1
        while i > 0 {
            best = max(best, bit[i])
            i -= i & -i
        }
        return best
    }
}
