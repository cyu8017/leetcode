// LeetCode 1389 - Create Target Array in the Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution {
    func createTargetArray(_ nums: [Int], _ index: [Int]) -> [Int] {
        var out = [Int]()
        for i in 0..<nums.count { out.insert(nums[i], at: index[i]) }
        return out
    }
}
