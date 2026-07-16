// LeetCode 0205 - Isomorphic Strings
// https://leetcode.com/problems/isomorphic-strings/

export function isIsomorphic(s: string, t: string): boolean {
    const forward = new Map<string, string>();
    const reverse = new Map<string, string>();

    for (let i = 0; i < s.length; i += 1) {
        const a = s[i];
        const b = t[i];
        if ((forward.has(a) && forward.get(a) !== b)
            || (reverse.has(b) && reverse.get(b) !== a)) {
            return false;
        }
        forward.set(a, b);
        reverse.set(b, a);
    }
    return true;
}