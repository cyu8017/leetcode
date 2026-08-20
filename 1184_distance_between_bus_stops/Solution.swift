// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

class Solution {
    func distanceBetweenBusStops(_ distance: [Int], _ start: Int, _ destination: Int) -> Int {
        var s = min(start, destination), d = max(start, destination)
        var clockwise = 0, total = 0
        for i in 0..<distance.count {
            total += distance[i]
            if i >= s && i < d { clockwise += distance[i] }
        }
        return min(clockwise, total - clockwise)
    }
}
