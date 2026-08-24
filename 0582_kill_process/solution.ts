// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

export function killProcess(pid: number[], ppid: number[], kill: number): number[] {
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
}
