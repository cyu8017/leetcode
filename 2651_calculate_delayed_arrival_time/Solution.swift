// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution {
    func findDelayedArrivalTime(_ arrivalTime: Int, _ delayedTime: Int) -> Int {
        (arrivalTime + delayedTime) % 24
    }
}
