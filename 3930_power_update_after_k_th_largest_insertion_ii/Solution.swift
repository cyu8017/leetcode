// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/


class Solution {
    func powerUpdate(_ nums: [Int], _ p: Int, _ queries: [[Int]]) -> [Int] {
        let mod = 1_000_000_007
        var vals = nums + queries.map { $0[0] }
        vals.sort()
        var uniq = 0
        for i in 0..<vals.count {
            if uniq == 0 || vals[i] != vals[uniq - 1] {
                vals[uniq] = vals[i]
                uniq += 1
            }
        }
        vals = Array(vals.prefix(uniq))
        var bit = Array(repeating: 0, count: vals.count + 1)
        func add(_ i0: Int) {
            var i = i0
            while i < bit.count {
                bit[i] += 1
                i += i & -i
            }
        }
        func lowerBound(_ x: Int) -> Int {
            var lo = 0, hi = vals.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if vals[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            return lo
        }
        func kth(_ rank0: Int) -> Int {
            var rank = rank0
            var idx = 0
            var step = 1
            while (step << 1) < bit.count { step <<= 1 }
            while step > 0 {
                let next = idx + step
                if next < bit.count && bit[next] < rank {
                    idx = next
                    rank -= bit[next]
                }
                step >>= 1
            }
            return vals[idx]
        }
        func powm(_ a0: Int, _ e0: Int) -> Int {
            var a = a0 % mod, e = e0, res = 1
            while e > 0 {
                if e & 1 != 0 { res = res * a % mod }
                a = a * a % mod
                e >>= 1
            }
            return res
        }
        for x in nums { add(lowerBound(x) + 1) }
        var ans = Array(repeating: 0, count: queries.count)
        var size = nums.count
        var cur = p
        for i in 0..<queries.count {
            add(lowerBound(queries[i][0]) + 1)
            size += 1
            let x = kth(size - queries[i][1] + 1)
            cur = powm(cur, x)
            ans[i] = cur
        }
        return ans
    }
}
