"use strict";
// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/
function sortArray(nums, pre) {
    const n = nums.length;
    const start = nums.join(",");
    const target = Array.from({ length: n }, (_, i) => i).join(",");
    if (start === target)
        return 0;
    const lengths = [...new Set(pre.filter((i) => i >= 2 && i <= n))].sort((a, b) => a - b);
    const visited = new Set([start]);
    let queue = [nums.slice()];
    let steps = 0;
    while (queue.length) {
        steps += 1;
        const nextQueue = [];
        for (const cur of queue) {
            for (const i of lengths) {
                const nxt = cur.slice(0, i).reverse().concat(cur.slice(i));
                const key = nxt.join(",");
                if (key === target)
                    return steps;
                if (!visited.has(key)) {
                    visited.add(key);
                    nextQueue.push(nxt);
                }
            }
        }
        queue = nextQueue;
    }
    return -1;
}
