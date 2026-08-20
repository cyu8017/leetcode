// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

function minimumSwap(s1: string, s2: string): number {
    let xy = 0, yx = 0;
    for (let i = 0; i < s1.length; i++) {
        if (s1[i] === "x" && s2[i] === "y") xy++;
        if (s1[i] === "y" && s2[i] === "x") yx++;
    }
    if ((xy + yx) % 2) return -1;
    return (xy >> 1) + (yx >> 1) + 2 * (xy % 2);
}
