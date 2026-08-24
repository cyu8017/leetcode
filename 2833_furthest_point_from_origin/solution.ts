// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

export function furthestDistanceFromOrigin(moves: string): number {
    let L = 0, R = 0, u = 0;
    for (const c of moves) {
        if (c === 'L') L++;
        else if (c === 'R') R++;
        else u++;
    }
    return Math.abs(L - R) + u;
}
