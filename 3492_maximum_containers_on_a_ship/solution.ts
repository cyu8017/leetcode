// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

export function maxContainers(n: any, w: any, maxWeight: any): any {
    const cap = n * n;
    const byW = Math.floor(maxWeight / w);
    return cap < byW ? cap : byW;
}
