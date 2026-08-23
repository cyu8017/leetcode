// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

/**
 * @param {string[]} arr
 * @return {string[]}
 */
var shortestSubstrings = function(arr) {
    const n = arr.length;
    const ans = new Array(n).fill("");
    for (let i = 0; i < n; i++) {
        const s = arr[i];
        const m = s.length;
        for (let j = 1; j <= m && ans[i] === ""; j++) {
            for (let l = 0; l <= m - j; l++) {
                const sub = s.substring(l, l + j);
                if (ans[i] === "" || ans[i] > sub) {
                    let ok = true;
                    for (let k = 0; k < n; k++) {
                        if (k !== i && arr[k].includes(sub)) { ok = false; break; }
                    }
                    if (ok) ans[i] = sub;
                }
            }
        }
    }
    return ans;
};
