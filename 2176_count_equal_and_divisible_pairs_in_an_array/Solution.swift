// LeetCode 2176 - Count Equal and Divisible Pairs in an Array
// https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution {
    func countPairs(_ nums: [Int], _ k: Int) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            for j in (i + 1)..<nums.count where nums[i] == nums[j] && (i * j) % k == 0 {
                ans += 1
            }
        }
        return ans
    }
}
