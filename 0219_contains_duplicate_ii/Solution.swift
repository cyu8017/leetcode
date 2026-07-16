// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

class Solution {
    func containsNearbyDuplicate(_ nums: [Int], _ k: Int) -> Bool {
        var lastIndex = [Int: Int]()
        for (i, num) in nums.enumerated() {
            if let prev = lastIndex[num], i - prev <= k {
                return true
            }
            lastIndex[num] = i
        }
        return false
    }
}
