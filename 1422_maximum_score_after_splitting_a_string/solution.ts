// LeetCode 1422: Maximum Score After Splitting A String

function maxScore(s: any): any {
    let ones = [...s].filter((ch: any): any => ch === "1").length, zeros = 0, best = 0;
    for (let i = 0; i < s.length - 1; i++) { if (s[i] === "0") zeros++; else ones--; best = Math.max(best, zeros + ones); }
    return best;
}
