// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

var minimumIndex = function(capacity, itemSize) {
    let ans = -1;
    for (let i = 0; i < capacity.length; i++) {
        if (capacity[i] >= itemSize && (ans === -1 || capacity[i] < capacity[ans])) ans = i;
    }
    return ans;
};
