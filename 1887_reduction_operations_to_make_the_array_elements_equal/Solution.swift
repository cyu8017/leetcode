// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution {
    func reductionOperations(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        var answer = 0
        var rank = 0

        for i in 1..<sorted.count {
            if sorted[i] != sorted[i - 1] {
                rank += 1
            }
            answer += rank
        }

        return answer
    }
}
