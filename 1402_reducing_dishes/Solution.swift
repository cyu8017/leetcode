// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

class Solution {
    func maxSatisfaction(_ satisfaction: [Int]) -> Int {
        var total = 0, answer = 0
        for value in satisfaction.sorted(by: >) {
            if total + value <= 0 { break }
            total += value
            answer += total
        }
        return answer
    }
}
