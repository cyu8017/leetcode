// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

function minDeletions(s: string): number {
    const count = new Map<string, number>();
    for (const ch of s) count.set(ch, (count.get(ch) || 0) + 1);
    const used = new Set<number>();
    let ans = 0;
    for (let x of count.values()) {
        while (x && used.has(x)) {
            x--;
            ans++;
        }
        used.add(x);
    }
    return ans;
}
