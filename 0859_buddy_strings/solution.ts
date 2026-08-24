// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

export function buddyStrings(s: string, goal: string): boolean {
    if (s.length !== goal.length) return false;
    if (s === goal) {
        const set = new Set();
        for (const ch of s) {
            if (set.has(ch)) return true;
            set.add(ch);
        }
        return false;
    }
    const diffs = [];
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== goal[i]) diffs.push([s[i], goal[i]]);
    }
    return diffs.length === 2 && diffs[0][0] === diffs[1][1] && diffs[0][1] === diffs[1][0];
}
