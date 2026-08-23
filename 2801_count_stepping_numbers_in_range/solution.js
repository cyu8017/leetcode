// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

/**
 * @param {string} low
 * @param {string} high
 * @return {number}
 */
var countSteppingNumbers = function(low, high) {
    const MOD = 1000000007;
    const dec = (s) => {
        const arr = s.split('');
        let i = arr.length - 1;
        while (i >= 0 && arr[i] === '0') {
            arr[i] = '9';
            i--;
        }
        if (i >= 0) arr[i] = String.fromCharCode(arr[i].charCodeAt(0) - 1);
        let j = 0;
        while (j < arr.length - 1 && arr[j] === '0') j++;
        return arr.slice(j).join('');
    };
    const countTo = (s) => {
        const memo = Array.from({length: 85}, () =>
            Array.from({length: 2}, () =>
                Array.from({length: 11}, () => Array(2).fill(-1))));
        const dfs = (pos, tight, last, started) => {
            if (pos === s.length) return started;
            if (memo[pos][tight][last + 1][started] !== -1) return memo[pos][tight][last + 1][started];
            const up = tight ? s.charCodeAt(pos) - 48 : 9;
            let ans = 0;
            for (let d = 0; d <= up; d++) {
                const nt = tight && d === up ? 1 : 0;
                if (!started) {
                    if (d === 0) ans += dfs(pos + 1, nt, -1, 0);
                    else ans += dfs(pos + 1, nt, d, 1);
                } else if (Math.abs(d - last) === 1) {
                    ans += dfs(pos + 1, nt, d, 1);
                }
            }
            return memo[pos][tight][last + 1][started] = ans % MOD;
        };
        return dfs(0, 1, -1, 0);
    };
    let ans = (countTo(high) - countTo(dec(low))) % MOD;
    if (ans < 0) ans += MOD;
    return ans;
};
