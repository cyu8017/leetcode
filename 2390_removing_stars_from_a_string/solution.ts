// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

export function removeStars(s: string): string {
    const stack = [];
    for (const c of s) {
        if (c === '*') stack.pop();
        else stack.push(c);
    }
    return stack.join('');
}
