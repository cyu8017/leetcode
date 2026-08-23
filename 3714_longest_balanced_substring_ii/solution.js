// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

var longestBalanced = function(s) {
    const calc1 = (str) => {
        let res = 0, n = str.length, i = 0;
        while (i < n) {
            let j = i + 1;
            while (j < n && str[j] === str[i]) j++;
            res = Math.max(res, j - i);
            i = j;
        }
        return res;
    };
    const calc2 = (str, a, b) => {
        let res = 0, n = str.length, i = 0;
        while (i < n) {
            while (i < n && str[i] !== a && str[i] !== b) i++;
            const pos = new Map();
            pos.set(0, i - 1);
            let d = 0;
            while (i < n && (str[i] === a || str[i] === b)) {
                if (str[i] === a) d++;
                else d--;
                if (pos.has(d)) res = Math.max(res, i - pos.get(d));
                else pos.set(d, i);
                i++;
            }
        }
        return res;
    };
    const calc3 = (str) => {
        const pos = new Map();
        pos.set('0,0', -1);
        const cnt = [0, 0, 0];
        let res = 0;
        for (let i = 0; i < str.length; i++) {
            cnt[str.charCodeAt(i) - 97]++;
            const x = cnt[0] - cnt[1], y = cnt[1] - cnt[2];
            const k = x + ',' + y;
            if (pos.has(k)) res = Math.max(res, i - pos.get(k));
            else pos.set(k, i);
        }
        return res;
    };
    const x = calc1(s);
    const y = Math.max(calc2(s, 'a', 'b'), Math.max(calc2(s, 'b', 'c'), calc2(s, 'a', 'c')));
    const z = calc3(s);
    return Math.max(x, Math.max(y, z));
};
