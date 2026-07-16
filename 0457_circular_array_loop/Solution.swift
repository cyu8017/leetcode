// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

class Solution {
    func circularArrayLoop(_ nums: [Int]) -> Bool {
        var values = nums
        let length = values.count

        func nextIndex(_ index: Int) -> Int {
            let next = index + values[index]
            return ((next % length) + length) % length
        }

        for start in 0..<length where values[start] != 0 {
            let forward = values[start] > 0
            var slow = start
            var fast = start
            var stop = false

            while !stop {
                slow = nextIndex(slow)
                fast = nextIndex(nextIndex(fast))
                if values[slow] * (forward ? 1 : -1) <= 0 ||
                    values[fast] * (forward ? 1 : -1) <= 0 ||
                    values[nextIndex(fast)] * (forward ? 1 : -1) <= 0 {
                    stop = true
                } else if slow == fast {
                    if slow == nextIndex(slow) {
                        stop = true
                    } else {
                        return true
                    }
                }
            }

            var index = start
            let direction = values[start]
            while values[index] * direction > 0 {
                values[index] = 0
                index = nextIndex(index)
            }
        }

        return false
    }
}
