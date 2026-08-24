// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

export function countCollisions(directions: string): number {
    let i = 0, j = directions.length - 1;
    while (i < directions.length && directions[i] === 'L') i++;
    while (j >= 0 && directions[j] === 'R') j--;
    let ans = 0;
    for (let k = i; k <= j; k++) if (directions[k] !== 'S') ans++;
    return ans;
}
