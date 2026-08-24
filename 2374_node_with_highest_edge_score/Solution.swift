// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

class Solution {
    func edgeScore(_ edges: [Int]) -> Int {
        let n = edges.count
        var score = [Int](repeating: 0, count: n)
        for i in 0..<n { score[edges[i]] += i }
        var ans = 0
        for i in 1..<n where score[i] > score[ans] { ans = i }
        return ans
    }
}
