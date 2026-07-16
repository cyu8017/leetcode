// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    const buckets = new Array(citations.length + 1).fill(0);
    for (const citation of citations) {
        buckets[Math.min(citation, citations.length)] += 1;
    }
    let total = 0;
    for (let h = buckets.length - 1; h >= 0; h--) {
        total += buckets[h];
        if (total >= h) {
            return h;
        }
    }
    return 0;
};
