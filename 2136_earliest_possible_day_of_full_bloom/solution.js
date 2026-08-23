// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

/**
 * @param {number[]} plantTime
 * @param {number[]} growTime
 * @return {number}
 */
var earliestFullBloom = function(plantTime, growTime) {
    const n = plantTime.length;
    const idx = Array.from({length: n}, (_, i) => i);
    idx.sort((a, b) => growTime[b] - growTime[a]);
    let day = 0, ans = 0;
    for (const i of idx) {
        day += plantTime[i];
        ans = Math.max(ans, day + growTime[i]);
    }
    return ans;
};
