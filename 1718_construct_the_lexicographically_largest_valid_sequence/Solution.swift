// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution {
    func constructDistancedSequence(_ n: Int) -> [Int] {
        var ans = [Int](repeating: 0, count: 2 * n - 1)
        var used = [Bool](repeating: false, count: n + 1)

        func backtrack(_ start: Int) -> Bool {
            var i = start
            while i < ans.count && ans[i] != 0 {
                i += 1
            }
            if i == ans.count {
                return true
            }
            for value in stride(from: n, through: 1, by: -1) {
                if used[value] {
                    continue
                }
                if value == 1 {
                    ans[i] = 1
                    used[1] = true
                    if backtrack(i + 1) {
                        return true
                    }
                    used[1] = false
                    ans[i] = 0
                } else {
                    let j = i + value
                    if j < ans.count && ans[j] == 0 {
                        ans[i] = value
                        ans[j] = value
                        used[value] = true
                        if backtrack(i + 1) {
                            return true
                        }
                        used[value] = false
                        ans[i] = 0
                        ans[j] = 0
                    }
                }
            }
            return false
        }

        _ = backtrack(0)
        return ans
    }
}
