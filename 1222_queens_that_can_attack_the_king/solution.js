// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

/**
 * @param {number[][]} queens
 * @param {number[]} king
 * @return {number[][]}
 */
var queensAttacktheKing = function(queens, king) {
    const occupied = new Set(queens.map((q) => q[0] + "," + q[1]));
    const answer = [];
    for (let dr = -1; dr <= 1; dr++) {
        for (let dc = -1; dc <= 1; dc++) {
            if (dr === 0 && dc === 0) continue;
            let r = king[0] + dr, c = king[1] + dc;
            while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                if (occupied.has(r + "," + c)) {
                    answer.push([r, c]);
                    break;
                }
                r += dr;
                c += dc;
            }
        }
    }
    return answer;
};
