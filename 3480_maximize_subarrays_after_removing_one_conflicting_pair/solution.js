// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

var maxSubarrays = function(n, conflictingPairs) {
    const m = conflictingPairs.length;
    let best = 0;
    for (let skip = 0; skip < m; skip++) {
        const rightLimit = new Array(n + 2).fill(n + 1);
        for (let i = 0; i < m; i++) {
            if (i === skip) continue;
            let a = conflictingPairs[i][0], b = conflictingPairs[i][1];
            if (a > b) { const t = a; a = b; b = t; }
            if (b < rightLimit[a]) rightLimit[a] = b;
        }
        let minRight = n + 1;
        let cnt = 0;
        for (let l = n; l >= 1; l--) {
            if (rightLimit[l] < minRight) minRight = rightLimit[l];
            cnt += minRight - l;
        }
        if (cnt > best) best = cnt;
    }
    return best;
};
