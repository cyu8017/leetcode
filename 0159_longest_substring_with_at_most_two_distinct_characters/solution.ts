// LeetCode 0159 - Longest Substring with At Most Two Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

export function lengthOfLongestSubstringTwoDistinct(s: string): number {
    const counts = new Map<string, number>();
    let left = 0;
    let best = 0;

    for (let right = 0; right < s.length; right += 1) {
        counts.set(s[right], (counts.get(s[right]) ?? 0) + 1);

        while (counts.size > 2) {
            const char = s[left];
            const count = counts.get(char)! - 1;
            if (count === 0) counts.delete(char);
            else counts.set(char, count);
            left += 1;
        }

        best = Math.max(best, right - left + 1);
    }

    return best;
}