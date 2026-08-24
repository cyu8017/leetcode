// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

export function repeatedCharacter(s: string): string {
    const seen = Array(26).fill(false);
    for (const c of s) {
        const i = c.charCodeAt(0) - 97;
        if (seen[i]) return c;
        seen[i] = true;
    }
    return String.fromCharCode(0);
}
