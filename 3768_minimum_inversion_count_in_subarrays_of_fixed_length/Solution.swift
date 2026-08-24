// LeetCode 3768 - Minimum Inversion Count In Subarrays Of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

class Solution {
    private var bit = [Int]()

    func minInversionCount(_ nums: [Int], _ k: Int) -> Int {
        var vals = nums.sorted()
        let u = unique(&vals)
        vals = Array(vals.prefix(u))
        bit = [Int](repeating: 0, count: vals.count + 1)
        var rank = [Int](repeating: 0, count: nums.count)
        var inv = 0
        for i in 0..<nums.count {
            rank[i] = lowerBound(vals, nums[i]) + 1
            if i < k {
                inv += i - sum(rank[i])
                add(rank[i], 1)
            }
        }
        var best = inv
        if nums.count > k {
            for r in k..<nums.count {
                let left = rank[r - k]
                inv -= sum(left - 1)
                add(left, -1)
                inv += k - 1 - sum(rank[r])
                add(rank[r], 1)
                if inv < best { best = inv }
            }
        }
        return best
    }

    private func add(_ i: Int, _ delta: Int) {
        var i = i
        while i < bit.count {
            bit[i] += delta
            i += i & -i
        }
    }

    private func sum(_ i: Int) -> Int {
        var i = i, res = 0
        while i > 0 {
            res += bit[i]
            i -= i & -i
        }
        return res
    }

    private func unique(_ a: inout [Int]) -> Int {
        var n = 0
        for i in 0..<a.count {
            if n == 0 || a[i] != a[n - 1] {
                a[n] = a[i]
                n += 1
            }
        }
        return n
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
