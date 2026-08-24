// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

export function exclusiveTime(n: number, logs: string[]): number[] {
    const result = Array(n).fill(0);
    const stack = [];
    let prevTime = 0;
    for (const log of logs) {
        const parts = log.split(":");
        const funcId = Number(parts[0]);
        const event = parts[1];
        const time = Number(parts[2]);
        if (event === "start") {
            if (stack.length) result[stack[stack.length - 1]] += time - prevTime;
            stack.push(funcId);
            prevTime = time;
        } else {
            result[stack.pop()] += time - prevTime + 1;
            prevTime = time + 1;
        }
    }
    return result;
}
