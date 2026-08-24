// LeetCode 2877 - Create a DataFrame from List
// https://leetcode.com/problems/create-a-dataframe-from-list/
// Pandas stand-in.

class Solution {
    func createDataframe(_ studentData: [[Int]]) -> [[String: Int]] {
        return studentData.map { ["student_id": $0[0], "age": $0[1]] }
    }
}
