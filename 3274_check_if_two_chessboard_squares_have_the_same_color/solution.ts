// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

export function checkTwoChessboards(coordinate1: any, coordinate2: any): any {
    const c1 = (coordinate1.charCodeAt(0) - 97) + (coordinate1.charCodeAt(1) - 49);
    const c2 = (coordinate2.charCodeAt(0) - 97) + (coordinate2.charCodeAt(1) - 49);
    return c1 % 2 === c2 % 2;
}
