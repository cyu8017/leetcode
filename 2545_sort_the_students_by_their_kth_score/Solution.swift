// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution {
    func sortTheStudents(_ score: [[Int]], _ k: Int) -> [[Int]] {
        score.sorted { $0[k] > $1[k] }
    }
}
