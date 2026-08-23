// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLengthOfOptimalCompression = function(s, k) {
    const memo = new Map();
    const dp = (index, remaining) => {
        if (remaining < 0) return 1e9;
        if (index === s.length || s.length - index <= remaining) return 0;
        const key = index + "," + remaining;
        if (memo.has(key)) return memo.get(key);
        let answer = dp(index + 1, remaining - 1);
        let same = 0, removed = 0;
        for (let j = index; j < s.length; j++) {
            if (s[j] === s[index]) {
                same++;
                const encoded = 1 + (same >= 2 ? 1 : 0) + (same >= 10 ? 1 : 0) + (same >= 100 ? 1 : 0);
                answer = Math.min(answer, encoded + dp(j + 1, remaining - removed));
            } else {
                removed++;
                if (removed > remaining) break;
            }
        }
        memo.set(key, answer);
        return answer;
    };
    return dp(0, k);
};
