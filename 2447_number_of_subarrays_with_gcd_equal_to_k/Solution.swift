// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

class Solution {
    func subarrayGCD(_ nums: [Int], _ k: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            var g = 0
            for j in i..<n {
                g = gcd(g, nums[j])
                if g < k { break }
                if g == k { ans += 1 }
            }
        }
        return ans
    }
}
