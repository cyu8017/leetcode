// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count_distinct_integers_after_removing_zeros/

var countDistinct = function(n) {
    const s = String(n);
    const m = s.length;
    const f = Array.from({length: 20}, () =>
        Array.from({length: 2}, () =>
            Array.from({length: 2}, () => new Array(2).fill(-1))));
    const dfs = (i, zero, lead, limit) => {
        if (i === m) return (zero === 0 && lead === 0) ? 1 : 0;
        if (limit === 0 && f[i][zero][lead][limit] !== -1) return f[i][zero][lead][limit];
        const up = limit === 1 ? s.charCodeAt(i) - 48 : 9;
        let ans = 0;
        for (let d = 0; d <= up; d++) {
            let nxtZero = zero;
            if (d === 0 && lead === 0) nxtZero = 1;
            const nxtLead = (lead === 1 && d === 0) ? 1 : 0;
            const nxtLimit = (limit === 1 && d === up) ? 1 : 0;
            ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit);
        }
        if (limit === 0) f[i][zero][lead][limit] = ans;
        return ans;
    };
    return dfs(0, 0, 1, 1);
};
