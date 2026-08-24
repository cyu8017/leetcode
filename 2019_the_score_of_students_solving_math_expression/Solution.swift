// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

class Solution {
    func scoreOfStudents(_ s: String, _ answers: [Int]) -> Int {
        let chars = Array(s)
        let n = chars.count
        let correct = evalCorrect(chars)
        var memo = [[Set<Int>?]](repeating: [Set<Int>?](repeating: nil, count: n), count: n)
        func dfs(_ l: Int, _ r: Int) -> Set<Int> {
            if let cached = memo[l][r] { return cached }
            var res = Set<Int>()
            if l == r {
                res.insert(Int(chars[l].asciiValue! - 48))
                memo[l][r] = res
                return res
            }
            var i = l + 1
            while i < r {
                for a in dfs(l, i - 1) {
                    for b in dfs(i + 1, r) {
                        let v = chars[i] == "+" ? a + b : a * b
                        if v <= 1000 { res.insert(v) }
                    }
                }
                i += 2
            }
            memo[l][r] = res
            return res
        }
        let possible = dfs(0, n - 1)
        var ans = 0
        for a in answers {
            if a == correct { ans += 5 }
            else if possible.contains(a) { ans += 2 }
        }
        return ans
    }

    private func evalCorrect(_ s: [Character]) -> Int {
        var nums = [Int]()
        var ops = [Character]()
        for c in s {
            if c >= "0" && c <= "9" { nums.append(Int(c.asciiValue! - 48)) }
            else { ops.append(c) }
        }
        var newNums = [nums[0]]
        var newOps = [Character]()
        for j in 0..<ops.count {
            if ops[j] == "*" {
                newNums[newNums.count - 1] *= nums[j + 1]
            } else {
                newOps.append(ops[j])
                newNums.append(nums[j + 1])
            }
        }
        var res = newNums[0]
        for j in 0..<newOps.count { res += newNums[j + 1] }
        return res
    }
}
