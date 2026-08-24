// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

export function shortestBeautifulSubstring(s: string, k: number): string {
    let ans = '';
    const n = s.length;
    for (let i = 0; i < n; i++) {
        let ones = 0;
        for (let j = i; j < n; j++) {
            if (s[j] === '1') ones++;
            if (ones === k) {
                const cand = s.slice(i, j + 1);
                if (!ans || cand.length < ans.length || (cand.length === ans.length && cand < ans))
                    ans = cand;
                break;
            }
            if (ones > k) break;
        }
    }
    return ans;
}
