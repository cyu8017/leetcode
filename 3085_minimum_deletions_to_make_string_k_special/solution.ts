// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

export function minimumDeletions(word: string, k: number): number {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < word.length; i++) freq[word.charCodeAt(i) - 97]++;
    const nums = freq.filter(v => v > 0);
    let ans = word.length;
    for (let i = 0; i <= word.length; i++) {
        let cur = 0;
        for (const x of nums) {
            if (x < i) cur += x;
            else if (x > i + k) cur += x - i - k;
        }
        ans = Math.min(ans, cur);
    }
    return ans;
}
