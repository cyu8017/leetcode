// LeetCode 2139 - Minimum Moves to Reach Target Score
// https://leetcode.com/problems/minimum-moves-to-reach-target-score/

export function minMoves(target: number, maxDoubles: number): number {
    let ans = 0;
    while (target > 1 && maxDoubles > 0) {
        if (target % 2 !== 0) { target--; ans++; }
        else { target = Math.floor(target / 2); maxDoubles--; ans++; }
    }
    return ans + target - 1;
}
