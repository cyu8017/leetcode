// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

/**
 * @param {string} s
 * @param {number} minJump
 * @param {number} maxJump
 * @return {boolean}
 */
var canReach = function(s, minJump, maxJump) {
    const n = s.length;
    const reachable = new Array(n).fill(false);
    reachable[0] = true;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        if (i > 0 && s[i] === "0") {
            const left = Math.max(0, i - maxJump);
            const right = i - minJump;
            if (right >= left && prefix[right + 1] - prefix[left] > 0) {
                reachable[i] = true;
            }
        }
        prefix[i + 1] = prefix[i] + (reachable[i] ? 1 : 0);
    }
    return reachable[n - 1];
};
