// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

export function finalPositionOfSnake(n: any, commands: any): any {
    let x = 0, y = 0;
    for (const c of commands) {
        if (c[0] === 'U') x--;
        else if (c[0] === 'D') x++;
        else if (c[0] === 'L') y--;
        else if (c[0] === 'R') y++;
    }
    return x * n + y;
}
