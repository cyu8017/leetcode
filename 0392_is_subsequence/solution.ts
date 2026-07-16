// LeetCode 0392 - Is Subsequence
export function isSubsequence(s: string, t: string): boolean {
    let index = 0;
    for (const char of t) {
        if (index < s.length && s[index] === char) index += 1;
    }
    return index === s.length;
}
