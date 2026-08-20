// LeetCode 1313 - Decompress Run-Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution {
    func decompressRLElist(_ nums: [Int]) -> [Int] {
        var answer = [Int](), i = 0
        while i < nums.count {
            answer.append(contentsOf: Array(repeating: nums[i + 1], count: nums[i]))
            i += 2
        }
        return answer
    }
}
