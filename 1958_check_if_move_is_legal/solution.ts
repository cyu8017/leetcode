// LeetCode 1958 - Check if Move is Legal
// https://leetcode.com/problems/check-if-move-is-legal/

function checkMove(board: any[][], rMove: number, cMove: number, color: any): boolean {
    const opp = color === "B" ? "W" : "B";
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]];
    for (const [dr, dc] of dirs) {
        let r = rMove + dr, c = cMove + dc, steps = 0;
        while (r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] === opp) {
            r += dr;
            c += dc;
            steps++;
        }
        if (steps && r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] === color) return true;
    }
    return false;
}
