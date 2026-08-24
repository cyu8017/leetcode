// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution {
    func kthSmallestPrimeFraction(_ arr: [Int], _ k: Int) -> [Int] {
        let n = arr.count
        var lo = 0.0, hi = 1.0
        var best = [0, 1]
        while true {
            let mid = (lo + hi) / 2.0
            var count = 0
            var j = 1
            var num = 0, den = 1
            for i in 0..<n {
                while j < n && Double(arr[i]) > mid * Double(arr[j]) { j += 1 }
                count += n - j
                if j < n && num * arr[j] < den * arr[i] {
                    num = arr[i]
                    den = arr[j]
                }
            }
            if count == k {
                return [num, den]
            } else if count < k {
                lo = mid
            } else {
                hi = mid
                best = [num, den]
            }
            if abs(hi - lo) < 1e-12 { return best }
        }
    }
}
