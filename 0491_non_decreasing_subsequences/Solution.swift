// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

class Solution {
    func findSubsequences(_ nums: [Int]) -> [[Int]] {
        var result: Set<[Int]> = []

        func backtrack(_ start: Int, _ path: inout [Int]) {
            if path.count >= 2 {
                result.insert(path)
            }
            var used: Set<Int> = []
            if start < nums.count {
                for index in start..<nums.count {
                    if used.contains(nums[index]) {
                        continue
                    }
                    if !path.isEmpty && nums[index] < path[path.count - 1] {
                        continue
                    }
                    used.insert(nums[index])
                    path.append(nums[index])
                    backtrack(index + 1, &path)
                    path.removeLast()
                }
            }
        }

        var path: [Int] = []
        backtrack(0, &path)
        return result.sorted()
    }
}
