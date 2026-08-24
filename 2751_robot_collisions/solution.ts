// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

export function survivedRobotsHealths(positions: number[], healths: number[], directions: string): number[] {
    const n = positions.length;
    const idx = Array.from({length: n}, (_, i) => i);
    idx.sort((a, b) => positions[a] - positions[b]);
    const stack = [];
    for (const i of idx) {
        const cur = [i, healths[i], directions[i]];
        while (stack.length && stack[stack.length - 1][2] === 'R' && cur[2] === 'L') {
            const top = stack[stack.length - 1];
            if (top[1] === cur[1]) {
                stack.pop();
                cur[1] = 0;
                break;
            } else if (top[1] > cur[1]) {
                top[1]--;
                cur[1] = 0;
                break;
            } else {
                cur[1]--;
                stack.pop();
            }
        }
        if (cur[1] > 0) stack.push(cur);
    }
    const alive = new Map();
    for (const [i, h] of stack) alive.set(i, h);
    const ans = [];
    for (let i = 0; i < n; i++) if (alive.has(i)) ans.push(alive.get(i));
    return ans;
}
