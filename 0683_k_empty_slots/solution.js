// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

/**
 * @param {number[]} bulbs
 * @param {number} k
 * @return {number}
 */
var kEmptySlots = function(bulbs, k) {
    const n = bulbs.length;
    const days = new Array(n).fill(0);
    for (let day = 1; day <= n; day++) days[bulbs[day - 1] - 1] = day;
    let ans = Infinity;
    let i = 0;
    while (i < n - k - 1) {
        const left = i, right = i + k + 1;
        let j = left + 1;
        while (j < right && days[j] > days[left] && days[j] > days[right]) j++;
        if (j === right) {
            ans = Math.min(ans, Math.max(days[left], days[right]));
            i++;
        } else i = j;
    }
    return ans === Infinity ? -1 : ans;
};
