// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

/**
 * @param {string} hamsters
 * @return {number}
 */
var minimumBuckets = function(hamsters) {
    const b = hamsters.split('');
    let ans = 0;
    for (let i = 0; i < b.length; i++) {
        if (b[i] !== 'H') continue;
        if (i > 0 && b[i - 1] === 'B') continue;
        if (i + 1 < b.length && b[i + 1] === '.') { b[i + 1] = 'B'; ans++; }
        else if (i > 0 && b[i - 1] === '.') { b[i - 1] = 'B'; ans++; }
        else return -1;
    }
    return ans;
};
