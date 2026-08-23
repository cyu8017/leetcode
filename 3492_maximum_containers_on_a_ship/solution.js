// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

var maxContainers = function(n, w, maxWeight) {
    const cap = n * n;
    const byW = Math.floor(maxWeight / w);
    return cap < byW ? cap : byW;
};
