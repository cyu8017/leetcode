// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution {
    func getMaxLen(_ nums: [Int]) -> Int {
        var positive = 0, negative = 0, answer = 0
        for x in nums {
            if x == 0 {
                positive = 0; negative = 0
            } else if x > 0 {
                positive += 1
                negative = negative > 0 ? negative + 1 : 0
            } else {
                let newPos = negative > 0 ? negative + 1 : 0
                negative = positive + 1
                positive = newPos
            }
            answer = max(answer, positive)
        }
        return answer
    }
}
