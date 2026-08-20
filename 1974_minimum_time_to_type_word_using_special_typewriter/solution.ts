// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

function minTimeToType(word: string): number {
    let cur = "a", ans = 0;
    for (const ch of word) {
        const d = Math.abs(ch.charCodeAt(0) - cur.charCodeAt(0));
        ans += Math.min(d, 26 - d) + 1;
        cur = ch;
    }
    return ans;
}
