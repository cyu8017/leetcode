// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution {
    func countStudents(_ students: [Int], _ sandwiches: [Int]) -> Int {
        var c = [0, 0]
        for s in students { c[s] += 1 }
        for (i, x) in sandwiches.enumerated() {
            if c[x] == 0 { return students.count - i }
            c[x] -= 1
        }
        return 0
    }
}
