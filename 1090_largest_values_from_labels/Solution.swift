// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

class Solution {
    func largestValsFromLabels(_ values: [Int], _ labels: [Int], _ numWanted: Int, _ useLimit: Int) -> Int {
        var items = zip(values, labels).map { ($0, $1) }
        items.sort { $0.0 > $1.0 }
        var used: [Int: Int] = [:]
        var ans = 0
        var taken = 0
        for (value, label) in items {
            if taken == numWanted { break }
            if used[label, default: 0] < useLimit {
                used[label, default: 0] += 1
                ans += value
                taken += 1
            }
        }
        return ans
    }
}
