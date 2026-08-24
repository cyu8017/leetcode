// LeetCode 0796 - Rotate String
// https://leetcode.com/problems/rotate-string/

export function rotateString(s: string, goal: string): boolean {
    return s.length === goal.length && (s + s).includes(goal);
}
