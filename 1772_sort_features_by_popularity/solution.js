// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

/**
 * @param {string[]} features
 * @param {string[]} responses
 * @return {string[]}
 */
var sortFeatures = function(features, responses) {
    const featureSet = new Set(features);
    const count = new Map();
    for (const response of responses) {
        const seen = new Set();
        for (const word of response.split(/\s+/)) {
            if (featureSet.has(word)) {
                seen.add(word);
            }
        }
        for (const word of seen) {
            count.set(word, (count.get(word) || 0) + 1);
        }
    }
    return [...features].sort((a, b) => {
        const ca = count.get(a) || 0;
        const cb = count.get(b) || 0;
        if (ca !== cb) {
            return cb - ca;
        }
        return a < b ? -1 : a > b ? 1 : 0;
    });
};
