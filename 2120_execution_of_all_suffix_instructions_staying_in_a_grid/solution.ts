// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

export function executeInstructions(n: number, startPos: number[], s: string): number[] {
    const m = s.length;
    const ans = new Array(m);
    for (let i = 0; i < m; i++) {
        let r = startPos[0], c = startPos[1], cnt = 0;
        for (let j = i; j < m; j++) {
            const ch = s[j];
            if (ch === 'L') c--;
            else if (ch === 'R') c++;
            else if (ch === 'U') r--;
            else r++;
            if (r < 0 || r >= n || c < 0 || c >= n) break;
            cnt++;
        }
        ans[i] = cnt;
    }
    return ans;
}
