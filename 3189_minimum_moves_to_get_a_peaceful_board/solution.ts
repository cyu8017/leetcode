// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

export function minMoves(rooks: any): any {
    let ans = 0;
    rooks.sort((a, b) => a[0] - b[0]);
    for (let i = 0; i < rooks.length; i++) ans += Math.abs(rooks[i][0] - i);
    rooks.sort((a, b) => a[1] - b[1]);
    for (let j = 0; j < rooks.length; j++) ans += Math.abs(rooks[j][1] - j);
    return ans;
}
