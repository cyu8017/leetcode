"use strict";
// LeetCode 1345 - Jump Game Iv
// https://leetcode.com/problems/jump-game-iv/
function minJumps(arr) {
    const positions = new Map();
    for (let i = 0; i < arr.length; i++) {
        if (!positions.has(arr[i]))
            positions.set(arr[i], []);
        positions.get(arr[i]).push(i);
    }
    const queue = [0], seen = new Set([0]);
    let steps = 0;
    while (queue.length) {
        const size = queue.length;
        for (let s = 0; s < size; s++) {
            const i = queue.shift();
            if (i === arr.length - 1)
                return steps;
            const next = (positions.get(arr[i]) || []).concat([i - 1, i + 1]);
            positions.delete(arr[i]);
            for (const j of next) {
                if (j >= 0 && j < arr.length && !seen.has(j)) {
                    seen.add(j);
                    queue.push(j);
                }
            }
        }
        steps++;
    }
    return -1;
}
