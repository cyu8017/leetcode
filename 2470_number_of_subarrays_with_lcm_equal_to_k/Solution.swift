// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

class Solution {
    func subarrayLCM(_ nums: [Int], _ k: Int) -> Int {
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
            var cur = 1
            for j in i..<n {
                cur = cur / gcd(cur, nums[j]) * nums[j]
                if cur > k { break }
                if cur == k { ans += 1 }
            }
        }
        return ans
    }
}
