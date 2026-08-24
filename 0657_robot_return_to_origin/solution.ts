// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/

export function judgeCircle(moves: string): boolean {
    let x = 0, y = 0;
    for (const move of moves) {
        if (move === "U") ++y;
        else if (move === "D") --y;
        else if (move === "L") --x;
        else if (move === "R") ++x;
    }
    return x === 0 && y === 0;
}
