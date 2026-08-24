// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

export function isReachableAtTime(sx: number, sy: number, fx: number, fy: number, t: number): boolean {
    const need = Math.max(Math.abs(sx - fx), Math.abs(sy - fy));
    if (need === 0) return t !== 1;
    return t >= need;
}
