// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution {
    func mostFrequent(_ nums: [Int], _ key: Int) -> Int {
        var freq = [Int: Int]()
        var best = 0, ans = 0
        for i in 0..<(nums.count - 1) where nums[i] == key {
            freq[nums[i + 1], default: 0] += 1
            if freq[nums[i + 1]]! > best {
                best = freq[nums[i + 1]]!
                ans = nums[i + 1]
            }
        }
        return ans
    }
}
