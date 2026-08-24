// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

export function maxCollectedFruits(fruits: any): any {
    const n = fruits.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans += fruits[i][i];
        fruits[i][i] = 0;
    }
    const neg = -(1 << 30);
    const dp2 = Array.from({length: n}, () => new Array(n).fill(neg));
    const dp3 = Array.from({length: n}, () => new Array(n).fill(neg));
    dp2[0][n - 1] = fruits[0][n - 1];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (dp2[i][j] === neg) continue;
            for (const dj of [-1, 0, 1]) {
                const ni = i + 1, nj = j + dj;
                if (ni < n && nj >= 0 && nj < n && nj > ni) {
                    const v = dp2[i][j] + fruits[ni][nj];
                    if (v > dp2[ni][nj]) dp2[ni][nj] = v;
                }
            }
        }
    }
    dp3[n - 1][0] = fruits[n - 1][0];
    for (let j = 0; j < n; j++) {
        for (let i = 0; i < n; i++) {
            if (dp3[i][j] === neg) continue;
            for (const di of [-1, 0, 1]) {
                const ni = i + di, nj = j + 1;
                if (ni >= 0 && ni < n && nj < n && ni > nj) {
                    const v = dp3[i][j] + fruits[ni][nj];
                    if (v > dp3[ni][nj]) dp3[ni][nj] = v;
                }
            }
        }
    }
    ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1];
    return ans;
}
