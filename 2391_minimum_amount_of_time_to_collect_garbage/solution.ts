// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

export function garbageCollection(garbage: string[], travel: number[]): number {
    let ans = 0;
    let lastM = 0, lastP = 0, lastG = 0;
    for (let i = 0; i < garbage.length; i++) {
        ans += garbage[i].length;
        for (let j = 0; j < garbage[i].length; j++) {
            const c = garbage[i][j];
            if (c === 'M') lastM = i;
            else if (c === 'P') lastP = i;
            else lastG = i;
        }
    }
    const pref = Array(travel.length + 1).fill(0);
    for (let i = 0; i < travel.length; i++) pref[i + 1] = pref[i] + travel[i];
    ans += pref[lastM] + pref[lastP] + pref[lastG];
    return ans;
}
