// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

class Solution {
    func topStudents(_ positive_feedback: [String], _ negative_feedback: [String], _ report: [String], _ student_id: [Int], _ k: Int) -> [Int] {
        let pos = Set(positive_feedback)
        let neg = Set(negative_feedback)
        var arr = [(Int, Int)]()
        for i in 0..<report.count {
            var score = 0
            for w in report[i].split(separator: " ") {
                let w = String(w)
                if pos.contains(w) { score += 3 }
                else if neg.contains(w) { score -= 1 }
            }
            arr.append((student_id[i], score))
        }
        arr.sort { $0.1 != $1.1 ? $0.1 > $1.1 : $0.0 < $1.0 }
        return Array(arr.prefix(k).map { $0.0 })
    }
}
