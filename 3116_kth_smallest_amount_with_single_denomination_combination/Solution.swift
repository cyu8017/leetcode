// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

class Solution {
    func findKthSmallest(_ coins: [Int], _ k: Int) -> Int {
        let n = coins.count
        var lo = 1, hi = 100_000_000_000
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if check(coins, n, mid, k) { hi = mid }
            else { lo = mid + 1 }
        }
        return lo
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a, y = b
        while y != 0 {
            let t = x % y
            x = y
            y = t
        }
        return x
    }

    private func check(_ coins: [Int], _ n: Int, _ mx: Int, _ k: Int) -> Bool {
        var cnt = 0
        for i in 1..<(1 << n) {
            var v = 1
            for j in 0..<n where ((i >> j) & 1) != 0 {
                v = v / gcd(v, coins[j]) * coins[j]
                if v > mx { break }
            }
            let m = i.nonzeroBitCount
            if m % 2 == 1 { cnt += mx / v }
            else { cnt -= mx / v }
        }
        return cnt >= k
    }
}
