// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

class Solution {
    func countDistinct(_ nums: [Int], _ k: Int, _ p: Int) -> Int {
        let n = nums.count
        var seen = Set<String>()
        for i in 0..<n {
            var div = 0
            var key = ""
            for j in i..<n {
                if nums[j] % p == 0 { div += 1 }
                if div > k { break }
                key += "\(nums[j] + 1),"
                seen.insert(key)
            }
        }
        return seen.count
    }
}
