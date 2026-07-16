// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

class Solution {
    func numberOfBoomerangs(_ points: [[Int]]) -> Int {
        var total = 0
        for anchor in points {
            var distances: [Int: Int] = [:]
            for other in points {
                let dx = anchor[0] - other[0]
                let dy = anchor[1] - other[1]
                let distance = dx * dx + dy * dy
                distances[distance, default: 0] += 1
            }
            for count in distances.values {
                total += count * (count - 1)
            }
        }
        return total
    }
}
