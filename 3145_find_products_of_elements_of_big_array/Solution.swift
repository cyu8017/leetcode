// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

class Solution {
    private let M = 50
    private var cnt = Array(repeating: 0, count: 51)
    private var s = Array(repeating: 0, count: 51)
    private var ready = false

    private func prepare() {
        if ready { return }
        var p = 1
        for i in 1...M {
            cnt[i] = cnt[i - 1] * 2 + p
            s[i] = s[i - 1] * 2 + p * (i - 1)
            p *= 2
        }
        ready = true
    }

    func findProductsOfElements(_ queries: [[Int]]) -> [Int] {
        prepare()
        return queries.map { q in
            let power = f(q[1] + 1) - f(q[0])
            return qpow(2, power, q[2])
        }
    }

    private func numIdxAndSum(_ x0: Int) -> (Int, Int) {
        var x = x0, idx = 0, totalSum = 0
        while x > 0 {
            let i = x.bitWidth - x.leadingZeroBitCount - 1
            idx += cnt[i]
            totalSum += s[i]
            x -= 1 << i
            totalSum += (x + 1) * i
            idx += x + 1
        }
        return (idx, totalSum)
    }

    private func f(_ i0: Int) -> Int {
        var l = 0, r = 1 << M
        while l < r {
            let mid = (l + r + 1) >> 1
            let p = numIdxAndSum(mid)
            if p.0 < i0 { l = mid }
            else { r = mid - 1 }
        }
        var p = numIdxAndSum(l)
        var totalSum = p.1
        var i = i0 - p.0
        var x = l + 1
        for _ in 0..<i {
            let y = x & -x
            totalSum += y.trailingZeroBitCount
            x -= y
        }
        return totalSum
    }

    private func qpow(_ a0: Int, _ n0: Int, _ mod: Int) -> Int {
        var ans = 1 % mod
        var a = a0 % mod
        var n = n0
        while n > 0 {
            if (n & 1) != 0 { ans = ans * a % mod }
            a = a * a % mod
            n >>= 1
        }
        return ans
    }
}
