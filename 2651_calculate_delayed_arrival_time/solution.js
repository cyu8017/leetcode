// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

var findDelayedArrivalTime = function(arrivalTime, delayedTime) {
    return (arrivalTime + delayedTime) % 24;
};
