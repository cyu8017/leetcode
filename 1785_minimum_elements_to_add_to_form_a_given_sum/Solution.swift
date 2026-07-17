// LeetCode 1785 - Minimum Elements to Add to Form a Given Sum
// https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

class Solution {
    func minElements(_ nums: [Int], _ limit: Int, _ goal: Int) -> Int {
        var sum = 0
        for num in nums {
            sum += num
        }
        let diff = abs(sum - goal)
        return (diff + limit - 1) / limit
    }
}
