// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

class Solution {
    func minRefuelStops(_ target: Int, _ startFuel: Int, _ stations: [[Int]]) -> Int {
        var all = stations
        all.append([target, 0])
        var heap = [Int]()
        var ans = 0, prev = 0, fuel = startFuel
        for st in all {
            let pos = st[0], gas = st[1]
            fuel -= pos - prev
            heap.sort()
            while !heap.isEmpty && fuel < 0 {
                fuel += heap.removeLast()
                ans += 1
            }
            if fuel < 0 { return -1 }
            heap.append(gas)
            prev = pos
        }
        return ans
    }
}
