// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

export function maxBottlesDrunk(numBottles: number, numExchange: number): number {
    let ans = numBottles;
    while (numBottles >= numExchange) {
        numBottles -= numExchange;
        numExchange++;
        ans++;
        numBottles++;
    }
    return ans;
}
