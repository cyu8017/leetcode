// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

class Solution {
    private class Fenwick {
        var f: [Int]
        init(_ n: Int) { f = [Int](repeating: 0, count: n) }
        func update(_ i: Int, _ val: Int) {
            var i = i
            while i < f.count {
                f[i] = max(f[i], val)
                i += i & -i
            }
        }
        func preMax(_ i: Int) -> Int {
            var i = i, res = 0
            while i > 0 {
                res = max(res, f[i])
                i &= i - 1
            }
            return res
        }
    }

    func maxAlternatingSum(_ nums: [Int], _ k: Int) -> Int {
        var sorted = nums.sorted()
        var m = 0
        for i in 0..<sorted.count {
            if i == 0 || sorted[i] != sorted[i - 1] {
                sorted[m] = sorted[i]
                m += 1
            }
        }
        sorted = Array(sorted.prefix(m))
        let n = nums.count
        var fInc = [Int](repeating: 0, count: n)
        var fDec = [Int](repeating: 0, count: n)
        let inc = Fenwick(m + 1)
        let dec = Fenwick(m + 1)
        var ans = 0
        var ranks = [Int](repeating: 0, count: n)
        for i in 0..<n {
            let x = nums[i]
            if i >= k {
                let j = ranks[i - k]
                inc.update(m - j, fInc[i - k])
                dec.update(j + 1, fDec[i - k])
            }
            var lo = 0, hi = sorted.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sorted[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            ranks[i] = lo
            fInc[i] = dec.preMax(lo) + x
            fDec[i] = inc.preMax(m - 1 - lo) + x
            ans = max(ans, max(fInc[i], fDec[i]))
        }
        return ans
    }
}
