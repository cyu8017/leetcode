// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

/**
 * @param {string} dominoes
 * @return {string}
 */
var pushDominoes = function(dominoes) {
    const arr = dominoes.split('');
    const n = arr.length;
    const force = new Array(n).fill(0);
    let f = 0;
    for (let i = 0; i < n; i++) {
        if (arr[i] === 'R') f = n;
        else if (arr[i] === 'L') f = 0;
        else f = Math.max(f - 1, 0);
        force[i] += f;
    }
    f = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (arr[i] === 'L') f = n;
        else if (arr[i] === 'R') f = 0;
        else f = Math.max(f - 1, 0);
        force[i] -= f;
    }
    for (let i = 0; i < n; i++) {
        if (force[i] > 0) arr[i] = 'R';
        else if (force[i] < 0) arr[i] = 'L';
        else arr[i] = '.';
    }
    return arr.join('');
};
