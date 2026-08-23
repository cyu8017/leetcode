// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

var isDigitorialPermutation = function(n) {
    const f = new Array(10).fill(0);
    f[0] = 1;
    for (let i = 1; i < 10; i++) f[i] = f[i - 1] * i;
    let x = 0, y = n;
    while (y > 0) {
        x += f[y % 10];
        y = Math.floor(y / 10);
    }
    const a = String(x).split('').sort().join('');
    const b = String(n).split('').sort().join('');
    return a === b;
};
