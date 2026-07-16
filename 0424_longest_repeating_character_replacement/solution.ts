// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

export class Solution {
    characterReplacement(s: string, k: number): number {
        const counts: Record<string, number> = {};
        let left = 0;
        let best = 0;
        let maxCount = 0;

        for (let right = 0; right < s.length; right += 1) {
            const char = s[right];
            counts[char] = (counts[char] || 0) + 1;
            maxCount = Math.max(maxCount, counts[char]);
            while ((right - left + 1) - maxCount > k) {
                counts[s[left]] -= 1;
                left += 1;
            }
            best = Math.max(best, right - left + 1);
        }

        return best;
    }
}
