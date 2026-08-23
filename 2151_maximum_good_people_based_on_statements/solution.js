// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

/**
 * @param {number[][]} statements
 * @return {number}
 */
var maximumGood = function(statements) {
    const n = statements.length;
    const ok = (mask) => {
        for (let i = 0; i < n; i++) {
            if ((mask & (1 << i)) === 0) continue;
            for (let j = 0; j < n; j++) {
                const s = statements[i][j];
                if (s === 2) continue;
                const goodJ = (mask & (1 << j)) !== 0;
                if ((s === 1 && !goodJ) || (s === 0 && goodJ)) return false;
            }
        }
        return true;
    };
    let ans = 0;
    for (let mask = 0; mask < (1 << n); mask++)
        if (ok(mask)) {
            let bc = 0, x = mask;
            while (x) { bc += x & 1; x >>= 1; }
            ans = Math.max(ans, bc);
        }
    return ans;
};
