// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

export function openLock(deadends: string[], target: string): number {
    const dead = new Set(deadends);
    if (dead.has('0000')) return -1;
    const q = ['0000'];
    const stepsQ = [0];
    const seen = new Set(['0000']);
    while (q.length > 0) {
        const state = q.shift();
        const steps = stepsQ.shift();
        if (state === target) return steps;
        const chars = state.split('');
        for (let i = 0; i < 4; i++) {
            const digit = chars[i].charCodeAt(0) - 48;
            for (const delta of [-1, 1]) {
                chars[i] = String((digit + delta + 10) % 10);
                const nxt = chars.join('');
                chars[i] = String(digit);
                if (!seen.has(nxt) && !dead.has(nxt)) {
                    seen.add(nxt);
                    q.push(nxt);
                    stepsQ.push(steps + 1);
                }
            }
        }
    }
    return -1;
}
