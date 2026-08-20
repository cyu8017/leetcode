// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

function findSmallestRegion(regions: string[][], region1: string, region2: string): string {
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
}
