// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

/**
 * @param {number[]} cookies
 * @param {number} k
 * @return {number}
 */
var distributeCookies = function(cookies, k) {
    const bags = Array(k).fill(0);
    let ans = Infinity;
    const dfs = (i) => {
        if (i === cookies.length) {
            let mx = 0;
            for (const b of bags) mx = Math.max(mx, b);
            ans = Math.min(ans, mx);
            return;
        }
        const seen = new Set();
        for (let j = 0; j < bags.length; ++j) {
            if (seen.has(bags[j])) continue;
            seen.add(bags[j]);
            bags[j] += cookies[i];
            if (bags[j] < ans) dfs(i + 1);
            bags[j] -= cookies[i];
            if (bags[j] === 0) break;
        }
    };
    dfs(0);
    return ans;
};
