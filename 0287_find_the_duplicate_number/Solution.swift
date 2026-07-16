// LeetCode 0287 - Find the Duplicate Number
// https://leetcode.com/problems/find-the-duplicate-number/

class Solution {
    func findDuplicate(_ nums: [Int]) -> Int {
        var slow = nums[0]
        var fast = nums[0]
        while true {
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast {
                break
            }
        }
        slow = nums[0]
        while slow != fast {
            slow = nums[slow]
            fast = nums[fast]
        }
        return slow
    }
}
