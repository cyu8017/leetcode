// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution {
    func frequencySort(_ nums: [Int]) -> [Int] {
        var count = [Int: Int]()
        for x in nums { count[x, default: 0] += 1 }
        return nums.sorted { a, b in
            if count[a]! != count[b]! { return count[a]! < count[b]! }
            return a > b
        }
    }
}
