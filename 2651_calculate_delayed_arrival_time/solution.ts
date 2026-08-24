// LeetCode 2651 - Calculate Delayed Arrival Time
// https://leetcode.com/problems/calculate-delayed-arrival-time/

export function findDelayedArrivalTime(arrivalTime: any, delayedTime: any): any {
    return (arrivalTime + delayedTime) % 24;
}
