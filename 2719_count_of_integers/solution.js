// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

var count = function(num1, num2, min_sum, max_sum) {
    const MOD = 1000000007;
    const dec = (s) => {
        const arr = s.split("");
        let i = arr.length - 1;
        while (i >= 0 && arr[i] === "0") { arr[i] = "9"; i--; }
        if (i >= 0) arr[i] = String.fromCharCode(arr[i].charCodeAt(0) - 1);
        let j = 0;
        while (j < arr.length - 1 && arr[j] === "0") j++;
        return arr.slice(j).join("");
    };
    const dp = (s) => {
        const memo = new Map();
        const dfs = (pos, sum, tight) => {
            if (sum > max_sum) return 0;
            if (pos === s.length) return sum >= min_sum ? 1 : 0;
            const key = pos + "," + sum + "," + (tight ? 1 : 0);
            if (memo.has(key)) return memo.get(key);
            const up = tight ? s.charCodeAt(pos) - 48 : 9;
            let res = 0;
            for (let d = 0; d <= up; d++)
                res = (res + dfs(pos + 1, sum + d, tight && d === up)) % MOD;
            memo.set(key, res);
            return res;
        };
        return dfs(0, 0, true);
    };
    return (dp(num2) - dp(dec(num1)) + MOD) % MOD;
};
