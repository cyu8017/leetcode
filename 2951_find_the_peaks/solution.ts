// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

export function findPeaks(mountain: any): any {
    const ans = [];
    for (let i = 1; i + 1 < mountain.length; i++)
        if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1])
            ans.push(i);
    return ans;
}
