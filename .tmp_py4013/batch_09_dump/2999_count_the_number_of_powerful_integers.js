// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

var numberOfPowerfulInt = function(start, finish, limit, s) {
    function count(num) {
        if (num < 0) return 0;
        for (let i = 0; i < s.length; i++) if (s.charCodeAt(i) - 48 > limit) return 0;
        const t = String(num);
        const n = t.length, sn = s.length;
        if (n < sn) return 0;
        let ans = 0;
        for (let length = sn; length < n; length++) {
            const preLen = length - sn;
            if (preLen === 0) ans += 1;
            else {
                let ways = limit;
                for (let i = 1; i < preLen; i++) ways *= (limit + 1);
                ans += ways;
            }
        }
        const pref = n - sn;
        const memo = new Map();
        function dfs(i, tight) {
            if (i === pref) {
                if (tight) return t.substring(pref) >= s ? 1 : 0;
                return 1;
            }
            const key = (i << 1) | (tight ? 1 : 0);
            if (memo.has(key)) return memo.get(key);
            let up = tight ? t.charCodeAt(i) - 48 : limit;
            if (up > limit) up = limit;
            let res = 0;
            for (let d = 0; d <= up; d++) {
                if (i === 0 && d === 0) continue;
                res += dfs(i + 1, tight && d === (t.charCodeAt(i) - 48));
            }
            memo.set(key, res);
            return res;
        }
        ans += dfs(0, true);
        return ans;
    }
    return count(finish) - count(start - 1);
};
