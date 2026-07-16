// LeetCode 0134 - Gas Station
// https://leetcode.com/problems/gas-station/

export function canCompleteCircuit(gas: number[], cost: number[]): number {
    let total = 0;
    let tank = 0;
    let start = 0;

    for (let i = 0; i < gas.length; i += 1) {
        const difference = gas[i] - cost[i];
        total += difference;
        tank += difference;
        if (tank < 0) {
            start = i + 1;
            tank = 0;
        }
    }

    return total >= 0 ? start : -1;
}