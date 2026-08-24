// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

export function findArray(pref: number[]): number[] {
    const ans = Array(pref.length);
    ans[0] = pref[0];
    for (let i = 1; i < pref.length; i++) ans[i] = pref[i] ^ pref[i - 1];
    return ans;
}
