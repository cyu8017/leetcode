// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

export function reachNumber(target: number): number {
    target = Math.abs(target);
    let steps = 0, total = 0;
    while (total < target || (total - target) % 2 !== 0) {
        steps++;
        total += steps;
    }
    return steps;
}
