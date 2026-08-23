// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

/**
 * @param {string} s
 * @param {number[]} answers
 * @return {number}
 */
var scoreOfStudents = function(s, answers) {
    const evalCorrect = (str) => {
        const nums = [], ops = [];
        for (const c of str) {
            if (c >= '0' && c <= '9') nums.push(c.charCodeAt(0) - 48);
            else ops.push(c);
        }
        const newNums = [nums[0]];
        const newOps = [];
        for (let j = 0; j < ops.length; j++) {
            if (ops[j] === '*') newNums[newNums.length - 1] *= nums[j + 1];
            else { newOps.push(ops[j]); newNums.push(nums[j + 1]); }
        }
        let res = newNums[0];
        for (let j = 0; j < newOps.length; j++) res += newNums[j + 1];
        return res;
    };
    const n = s.length;
    const correct = evalCorrect(s);
    const dp = Array.from({length: n}, () => new Array(n).fill(null));
    const dfs = (l, r) => {
        if (dp[l][r] !== null) return dp[l][r];
        const res = new Set();
        if (l === r) { res.add(s.charCodeAt(l) - 48); dp[l][r] = res; return res; }
        for (let i = l + 1; i < r; i += 2) {
            for (const a of dfs(l, i - 1))
                for (const b of dfs(i + 1, r)) {
                    const v = s[i] === '+' ? a + b : a * b;
                    if (v <= 1000) res.add(v);
                }
        }
        dp[l][r] = res;
        return res;
    };
    const possible = dfs(0, n - 1);
    let ans = 0;
    for (const a of answers) {
        if (a === correct) ans += 5;
        else if (possible.has(a)) ans += 2;
    }
    return ans;
};
