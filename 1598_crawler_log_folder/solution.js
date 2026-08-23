// LeetCode 1598 - Crawler Log Folder
// https://leetcode.com/problems/crawler-log-folder/

/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    let depth = 0;
    for (const log of logs) {
        if (log === "../") depth = Math.max(0, depth - 1);
        else if (log !== "./") depth++;
    }
    return depth;
};
