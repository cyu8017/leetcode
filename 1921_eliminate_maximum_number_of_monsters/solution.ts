// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

function eliminateMaximum(dist: number[], speed: number[]): number {
    const arrival = dist.map((d, i: any) => Math.ceil(d / speed[i])).sort((a, b: any) => a - b);
    for (let i = 0; i < arrival.length; i++) {
        if (arrival[i] <= i) return i;
    }
    return arrival.length;
}
