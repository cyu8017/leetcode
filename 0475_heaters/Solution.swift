// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

class Solution {
    func findRadius(_ houses: [Int], _ heaters: [Int]) -> Int {
        let sortedHeaters = heaters.sorted()
        var radius = 0
        for house in houses {
            let position = sortedHeaters.partitioningIndex { $0 < house }
            var distances: [Int] = []
            if position < sortedHeaters.count {
                distances.append(abs(sortedHeaters[position] - house))
            }
            if position > 0 {
                distances.append(abs(sortedHeaters[position - 1] - house))
            }
            radius = max(radius, distances.min() ?? 0)
        }
        return radius
    }
}
