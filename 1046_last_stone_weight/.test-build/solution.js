"use strict";
// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/
function lastStoneWeight(stones) {
    stones.sort((a, b) => a - b);
    while (stones.length > 1) {
        const a = stones.pop();
        const b = stones.pop();
        if (a !== b) {
            const diff = a - b;
            let i = 0;
            while (i < stones.length && stones[i] < diff)
                i++;
            stones.splice(i, 0, diff);
        }
    }
    return stones.length ? stones[0] : 0;
}
