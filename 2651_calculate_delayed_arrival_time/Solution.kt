// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution {
    fun findDelayedArrivalTime(arrivalTime: Int, delayedTime: Int): Int {
        return (arrivalTime + delayedTime) % 24
    }
}
