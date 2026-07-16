// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

class Solution {
    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        let sorted = nums.sorted()
        var result: [[Int]] = []
        var path: [Int] = []
        var used = Array(repeating: false, count: sorted.count)

        func backtrack() {
            if path.count == sorted.count {
                result.append(path)
                return
            }

            for i in 0..<sorted.count {
                if used[i] {
                    continue
                }
                if i > 0 && sorted[i] == sorted[i - 1] && !used[i - 1] {
                    continue
                }
                used[i] = true
                path.append(sorted[i])
                backtrack()
                path.removeLast()
                used[i] = false
            }
        }

        backtrack()
        return result
    }
}
