// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

var beautifulNumbers = function(l, r) {
    const countBeautiful = (n) => {
        if (n <= 0) return 0;
        const s = String(n);
        const dfs = (pos, tight, sum, prod, started) => {
            if (pos === s.length) {
                if (!started) return 0;
                return (sum > 0 && prod % sum === 0) ? 1 : 0;
            }
            const up = tight ? (s.charCodeAt(pos) - 48) : 9;
            let ans = 0;
            for (let d = 0; d <= up; d++) {
                const nt = tight && d === up;
                if (!started && d === 0) ans += dfs(pos + 1, nt, 0, 1, false);
                else {
                    const ns = sum + d;
                    const np = !started ? d : prod * d;
                    ans += dfs(pos + 1, nt, ns, np, true);
                }
            }
            return ans;
        };
        return dfs(0, true, 0, 1, false);
    };
    return countBeautiful(r) - countBeautiful(l - 1);
};
