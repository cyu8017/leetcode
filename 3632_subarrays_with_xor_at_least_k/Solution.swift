// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

class Solution {
    func subarraysWithXorAtLeastK(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var x = 0
            for j in i..<n {
                x ^= nums[j]
                if x >= k { ans += 1 }
            }
        }
        return ans
    }
}
