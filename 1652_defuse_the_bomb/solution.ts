// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

function decrypt(code: number[], k: number): number[] {
    const n = code.length;
    if (k === 0) return Array(n).fill(0);
    const a = code.concat(code);
    const ans: number[] = [];
    for (let i = 0; i < n; i++) {
        let sum = 0;
        if (k > 0) {
            for (let j = i + 1; j <= i + k; j++) sum += a[j];
        } else {
            for (let j = i + n + k; j < i + n; j++) sum += a[j];
        }
        ans.push(sum);
    }
    return ans;
}
