// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

/**
 * @param {number} memory1
 * @param {number} memory2
 * @return {number[]}
 */
var memLeak = function(memory1, memory2) {
    let second = 1;
    while (memory1 >= second || memory2 >= second) {
        if (memory1 >= memory2) memory1 -= second;
        else memory2 -= second;
        second++;
    }
    return [second, memory1, memory2];
};
