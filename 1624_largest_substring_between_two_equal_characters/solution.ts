// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

function maxLengthBetweenEqualCharacters(s: string): number {
    const first = new Map<string, number>();
    let ans = -1;
    for (let i = 0; i < s.length; i++) {
        if (first.has(s[i])) ans = Math.max(ans, i - first.get(s[i])! - 1);
        else first.set(s[i], i);
    }
    return ans;
}
