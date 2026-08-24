// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution {
    func findLongestChain(_ pairs: [[Int]]) -> Int {
        let pairs = pairs.sorted { $0[1] < $1[1] }
        var length = 0
        var currentEnd = Int.min
        for pair in pairs where pair[0] > currentEnd {
            length += 1
            currentEnd = pair[1]
        }
        return length
    }
}
