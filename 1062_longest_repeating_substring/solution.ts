// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

function longestRepeatingSubstring(s: string): number {
    const n = s.length;
    function hasDup(length: number): boolean {
        const seen = new Set<string>();
        for (let i = 0; i <= n - length; i++) {
            const sub = s.slice(i, i + length);
            if (seen.has(sub)) return true;
            seen.add(sub);
        }
        return false;
    }
    let lo = 1;
    let hi = n - 1;
    let ans = 0;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (hasDup(mid)) {
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return ans;
}
