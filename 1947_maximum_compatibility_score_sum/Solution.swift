// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

class Solution {
    func maxCompatibilitySum(_ students: [[Int]], _ mentors: [[Int]]) -> Int {
        let m = students.count
        var score = Array(repeating: Array(repeating: 0, count: m), count: m)
        for i in 0..<m {
            for j in 0..<m {
                score[i][j] = zip(students[i], mentors[j]).filter { $0 == $1 }.count
            }
        }
        var memo = [Int: Int]()
        func dp(_ i: Int, _ mask: Int) -> Int {
            if i == m { return 0 }
            let key = i * 1024 + mask
            if let v = memo[key] { return v }
            var best = 0
            for j in 0..<m where mask & (1 << j) == 0 {
                best = max(best, score[i][j] + dp(i + 1, mask | (1 << j)))
            }
            memo[key] = best
            return best
        }
        return dp(0, 0)
    }
}
