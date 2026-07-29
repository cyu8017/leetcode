// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

function smallestSubsequence(s: string): string {
    const last = new Map<string, number>();
    for (let i = 0; i < s.length; i++) last.set(s[i], i);
    const stack: string[] = [];
    const used = new Set<string>();
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (used.has(ch)) continue;
        while (stack.length && ch < stack[stack.length - 1] && last.get(stack[stack.length - 1])! > i) {
            used.delete(stack.pop()!);
        }
        stack.push(ch);
        used.add(ch);
    }
    return stack.join("");
}
