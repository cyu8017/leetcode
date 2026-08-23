// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

/**
 * @param {string} s
 * @return {number}
 */
var longestAwesome = function(s) {
    const first = new Map([[0, -1]]);
    let mask = 0, answer = 0;
    for (let i = 0; i < s.length; i++) {
        mask ^= 1 << (+s[i]);
        if (first.has(mask)) answer = Math.max(answer, i - first.get(mask));
        else first.set(mask, i);
        for (let bit = 0; bit < 10; bit++) {
            const candidate = mask ^ (1 << bit);
            if (first.has(candidate)) answer = Math.max(answer, i - first.get(candidate));
        }
    }
    return answer;
};
