// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

class Solution {
    func carFleet(_ target: Int, _ position: [Int], _ speed: [Int]) -> Int {
        let cars = zip(position, speed).sorted { $0.0 > $1.0 }
        var fleets = 0
        var maxTime = 0.0
        for car in cars {
            let time = Double(target - car.0) / Double(car.1)
            if time > maxTime {
                fleets += 1
                maxTime = time
            }
        }
        return fleets
    }
}
