// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

/**
 * @param {string} message
 * @param {number} limit
 * @return {string[]}
 */
var splitMessage = function(message, limit) {
    const n = message.length;
    for (let parts = 1; parts <= n; parts++) {
        const sbDigits = String(parts).length;
        let ok = true, idx = 0;
        const res = [];
        for (let i = 1; i <= parts; i++) {
            const tail = 3 + String(i).length + sbDigits;
            const cap = limit - tail;
            if (cap <= 0 || idx >= n) { ok = false; break; }
            let take = cap;
            if (take > n - idx) take = n - idx;
            res.push(message.substring(idx, idx + take) + '<' + i + '/' + parts + '>');
            idx += take;
        }
        if (ok && idx === n) return res;
    }
    return [];
};
