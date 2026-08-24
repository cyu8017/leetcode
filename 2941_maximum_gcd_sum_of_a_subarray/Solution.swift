// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

class Solution {
    func maxGcdSum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        var ans = 0
        var st: [(Int, Int)] = []
        for i in 0..<n {
            var nst: [(Int, Int)] = [(nums[i], i)]
            for p in st {
                let g = gcd(p.0, nums[i])
                if nst.last!.0 == g { continue }
                nst.append((g, p.1))
            }
            st = nst
            for p in st {
                let g = p.0, idx = p.1
                if i - idx + 1 >= k {
                    ans = max(ans, (pref[i + 1] - pref[idx]) * g)
                }
            }
        }
        return ans
    }

    private func gcd(_ a0: Int, _ b0: Int) -> Int {
        var a = a0, b = b0
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }
}
