// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

class Solution {
    func subsetsWithDup(_ nums: [Int]) -> [[Int]] {
        let sorted = nums.sorted()
        var result: [[Int]] = []
        var path: [Int] = []

        func backtrack(_ start: Int) {
            result.append(path)
            for i in start..<sorted.count {
                if i > start && sorted[i] == sorted[i - 1] {
                    continue
                }
                path.append(sorted[i])
                backtrack(i + 1)
                path.removeLast()
            }
        }

        backtrack(0)
        return result
    }
}
