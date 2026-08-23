// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    const index1 = new Map();
    for (let i = 0; i < list1.length; ++i) index1.set(list1[i], i);
    let best = Infinity;
    const answer = [];
    for (let j = 0; j < list2.length; ++j) {
        if (!index1.has(list2[j])) continue;
        const total = index1.get(list2[j]) + j;
        if (total < best) {
            best = total;
            answer.length = 0;
            answer.push(list2[j]);
        } else if (total === best) {
            answer.push(list2[j]);
        }
    }
    return answer;
};
