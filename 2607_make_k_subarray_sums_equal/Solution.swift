// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

class Solution {
    func makeSubKSumEqual(_ arr: [Int], _ k: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        let n = arr.count
        let g = gcd(n, k)
        var ans = 0
        for r in 0..<g {
            var group = [Int]()
            var i = r
            while i < n {
                group.append(arr[i])
                i += g
            }
            group.sort()
            let med = group[group.count / 2]
            for x in group { ans += abs(x - med) }
        }
        return ans
    }
}
