// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

function averageWaitingTime(customers: number[][]): number {
    let current = 0;
    let total = 0;
    for (const [arrival, cook] of customers) {
        current = Math.max(current, arrival) + cook;
        total += current - arrival;
    }
    return total / customers.length;
}
