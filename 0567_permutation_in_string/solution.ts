// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

export function checkInclusion(s1: string, s2: string): boolean {
    const n1 = s1.length, n2 = s2.length;
    if (n1 > n2) return false;
    const need = Array(26).fill(0);
    const window = Array(26).fill(0);
    for (let i = 0; i < n1; ++i) {
        ++need[s1.charCodeAt(i) - 97];
        ++window[s2.charCodeAt(i) - 97];
    }
    let matches = 0;
    for (let i = 0; i < 26; ++i) if (need[i] === window[i]) ++matches;
    if (matches === 26) return true;
    for (let right = n1; right < n2; ++right) {
        const add = s2.charCodeAt(right) - 97;
        const remove = s2.charCodeAt(right - n1) - 97;
        if (window[add] === need[add]) --matches;
        ++window[add];
        if (window[add] === need[add]) ++matches;
        if (window[remove] === need[remove]) --matches;
        --window[remove];
        if (window[remove] === need[remove]) ++matches;
        if (matches === 26) return true;
    }
    return false;
}
