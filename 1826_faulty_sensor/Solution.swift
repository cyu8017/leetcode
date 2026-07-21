// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

class Solution {
    func badSensor(_ sensor1: [Int], _ sensor2: [Int]) -> Int {
        if sensor1 == sensor2 { return -1 }

        func isDefective(_ correct: [Int], _ faulty: [Int]) -> Bool {
            let n = correct.count
            var i = 0
            while i < n && correct[i] == faulty[i] { i += 1 }
            if i == n { return false }
            var j = i
            while j < n - 1 && correct[j + 1] == faulty[j] { j += 1 }
            return j == n - 1
        }

        let sensor1Bad = isDefective(sensor2, sensor1)
        let sensor2Bad = isDefective(sensor1, sensor2)
        if sensor1Bad && sensor2Bad { return -1 }
        if sensor1Bad { return 1 }
        if sensor2Bad { return 2 }
        return -1
    }
}
