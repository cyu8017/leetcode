// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

class Solution {
    func partitionLabels(_ s: String) -> [Int] {
        let chars = Array(s)
        var last = [Character: Int]()
        for (i, ch) in chars.enumerated() { last[ch] = i }
        var result = [Int]()
        var start = 0, end = 0
        for (i, ch) in chars.enumerated() {
            end = max(end, last[ch]!)
            if i == end {
                result.append(end - start + 1)
                start = i + 1
            }
        }
        return result
    }
}
