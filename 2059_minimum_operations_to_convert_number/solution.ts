// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

export function minimumOperations(nums: number[], start: number, goal: number): number {
    if (start === goal) return 0;
    const vis = new Set([start]);
    const q = [start];
    let steps = 0;
    while (q.length) {
        steps++;
        let sz = q.length;
        while (sz-- > 0) {
            const cur = q.shift();
            for (const x of nums) {
                for (const nxt of [cur + x, cur - x, cur ^ x]) {
                    if (nxt === goal) return steps;
                    if (nxt >= 0 && nxt <= 1000 && !vis.has(nxt)) {
                        vis.add(nxt);
                        q.push(nxt);
                    }
                }
            }
        }
    }
    return -1;
}
