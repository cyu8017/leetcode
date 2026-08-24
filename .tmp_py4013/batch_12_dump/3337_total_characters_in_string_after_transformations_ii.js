// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

function matMul(a, b, mod) {
    const n = a.length;
    const c = Array.from({length: n}, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        for (let k = 0; k < n; k++) {
            if (a[i][k] === 0) continue;
            for (let j = 0; j < n; j++) {
                c[i][j] = (c[i][j] + a[i][k] * b[k][j] % mod) % mod;
            }
        }
    }
    return c;
}
function matPow(a, e, mod) {
    const n = a.length;
    let r = Array.from({length: n}, (_, i) => {
        const row = new Array(n).fill(0);
        row[i] = 1;
        return row;
    });
    while (e > 0) {
        if (e & 1) r = matMul(r, a, mod);
        a = matMul(a, a, mod);
        e >>= 1;
    }
    return r;
}
var lengthAfterTransformations = function(s, t, nums) {
    const mod = 1000000007;
    let mat = Array.from({length: 26}, () => new Array(26).fill(0));
    for (let i = 0; i < 26; i++) {
        for (let j = 1; j <= nums[i]; j++) mat[i][(i + j) % 26] = 1;
    }
    mat = matPow(mat, t, mod);
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let ans = 0;
    for (let i = 0; i < 26; i++) {
        for (let j = 0; j < 26; j++) {
            ans = (ans + cnt[i] * mat[i][j] % mod) % mod;
        }
    }
    return ans;
};
