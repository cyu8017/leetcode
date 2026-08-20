// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

class Solution {
    func uniqueOccurrences(_ arr: [Int]) -> Bool {
        var count: [Int: Int] = [:]
        for x in arr { count[x, default: 0] += 1 }
        let freqs = Array(count.values)
        return Set(freqs).count == freqs.count
    }
}
