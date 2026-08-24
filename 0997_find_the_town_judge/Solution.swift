// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

class Solution {
    func findJudge(_ n: Int, _ trust: [[Int]]) -> Int {
        var score = [Int](repeating: 0, count: n + 1)
        for t in trust {
            score[t[0]] -= 1
            score[t[1]] += 1
        }
        for i in 1...n where score[i] == n - 1 { return i }
        return -1
    }
}
