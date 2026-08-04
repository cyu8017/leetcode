// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

/**
 * @param {string[][]} regions
 * @param {string} region1
 * @param {string} region2
 * @return {string}
 */
var findSmallestRegion = function(regions, region1, region2) {
    const parent = new Map();
    for (const group of regions) {
        for (let i = 1; i < group.length; i++) parent.set(group[i], group[0]);
    }
    const ancestors = new Set();
    while (region1) {
        ancestors.add(region1);
        region1 = parent.get(region1);
    }
    while (!ancestors.has(region2)) region2 = parent.get(region2);
    return region2;
};
