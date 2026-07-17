// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

function areAlmostEqual(s1: string, s2: string): boolean {
    const diff: number[] = [];
    for (let i = 0; i < s1.length; i++) {
        if (s1[i] !== s2[i]) diff.push(i);
    }
    if (diff.length === 0) return true;
    return diff.length === 2 &&
        s1[diff[0]] === s2[diff[1]] &&
        s1[diff[1]] === s2[diff[0]];
}
