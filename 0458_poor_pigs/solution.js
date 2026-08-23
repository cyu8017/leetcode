// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

class Solution {
    poorPigs(buckets, minutesToDie, minutesToTest) {
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

module.exports = { Solution };
