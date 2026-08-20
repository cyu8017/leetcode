// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

function maxCompatibilitySum(students: number[][], mentors: number[][]): number {
    const m = students.length;
    const score = Array.from({ length: m }, () => new Array(m).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++) {
            let s = 0;
            for (let k = 0; k < students[i].length; k++) if (students[i][k] === mentors[j][k]) s++;
            score[i][j] = s;
        }
    }
    const memo = new Map();
    const dp = (i: any, mask: any) => {
        if (i === m) return 0;
        const key = `${i},${mask}`;
        if (memo.has(key)) return memo.get(key);
        let best = 0;
        for (let j = 0; j < m; j++) {
            if ((mask & (1 << j)) === 0) best = Math.max(best, score[i][j] + dp(i + 1, mask | (1 << j)));
        }
        memo.set(key, best);
        return best;
    };
    return dp(0, 0);
}
