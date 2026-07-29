// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

class Solution {
    func highFive(_ items: [[Int]]) -> [[Int]] {
        var scores: [Int: [Int]] = [:]
        for item in items {
            scores[item[0], default: []].append(item[1])
        }
        var ans: [[Int]] = []
        for studentId in scores.keys.sorted() {
            let top = scores[studentId]!.sorted(by: >).prefix(5)
            ans.append([studentId, top.reduce(0, +) / 5])
        }
        return ans
    }
}
