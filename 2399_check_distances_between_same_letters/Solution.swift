// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

class Solution {
    func checkDistances(_ s: String, _ distance: [Int]) -> Bool {
        var first = [Int](repeating: -1, count: 26)
        for (i, ch) in s.utf8.enumerated() {
            let c = Int(ch - 97)
            if first[c] == -1 { first[c] = i }
            else if i - first[c] - 1 != distance[c] { return false }
        }
        return true
    }
}
