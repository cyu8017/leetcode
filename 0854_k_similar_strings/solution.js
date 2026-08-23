// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var kSimilarity = function(s1, s2) {
    if (s1 === s2) return 0;
    const neighbors = (s) => {
        const arr = s.split('');
        let i = 0;
        while (arr[i] === s2[i]) i++;
        const res = [];
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] === s2[i] && arr[j] !== s2[j]) {
                [arr[i], arr[j]] = [arr[j], arr[i]];
                res.push(arr.join(''));
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }
        return res;
    };
    const queue = [s1];
    const dist = new Map([[s1, 0]]);
    while (queue.length) {
        const cur = queue.shift();
        const d = dist.get(cur);
        for (const nxt of neighbors(cur)) {
            if (nxt === s2) return d + 1;
            if (!dist.has(nxt)) {
                dist.set(nxt, d + 1);
                queue.push(nxt);
            }
        }
    }
    return -1;
};
