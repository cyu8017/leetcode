// LeetCode 1422: Maximum Score After Splitting A String

var maxScore = function(s) {
    let ones = [...s].filter(ch => ch === "1").length, zeros = 0, best = 0;
    for (let i = 0; i < s.length - 1; i++) { if (s[i] === "0") zeros++; else ones--; best = Math.max(best, zeros + ones); }
    return best;
};
