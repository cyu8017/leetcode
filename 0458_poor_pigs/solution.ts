// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

export class Solution {
    poorPigs(buckets: number, minutesToDie: number, minutesToTest: number): number {
        const states = Math.floor(minutesToTest / minutesToDie) + 1;
        let pigs = 0;
        let capacity = 1;
        while (capacity < buckets) {
            pigs += 1;
            capacity *= states;
        }
        return pigs;
    }
}
