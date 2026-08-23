// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

/**
 * @param {number[]} pid
 * @param {number[]} ppid
 * @param {number} kill
 * @return {number[]}
 */
var killProcess = function(pid, ppid, kill) {
    const children = new Map();
    for (let i = 0; i < pid.length; ++i) {
        if (!children.has(ppid[i])) children.set(ppid[i], []);
        children.get(ppid[i]).push(pid[i]);
    }
    const result = [];
    const queue = [kill];
    while (queue.length) {
        const process = queue.shift();
        result.push(process);
        const kids = children.get(process);
        if (kids) for (const child of kids) queue.push(child);
    }
    return result;
};
