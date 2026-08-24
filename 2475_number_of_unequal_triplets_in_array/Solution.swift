// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

class Solution {
    func unequalTriplets(_ nums: [Int]) -> Int {
        var cnt = [Int: Int]()
        for x in nums { cnt[x, default: 0] += 1 }
        var ans = 0, left = 0
        let n = nums.count
        for c in cnt.values {
            let right = n - left - c
            ans += left * c * right
            left += c
        }
        return ans
    }
}
