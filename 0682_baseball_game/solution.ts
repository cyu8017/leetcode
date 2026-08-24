// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

export function calPoints(operations: string[]): number {
    const stack = [];
    for (const op of operations) {
        if (op === 'C') stack.pop();
        else if (op === 'D') stack.push(stack[stack.length - 1] * 2);
        else if (op === '+') stack.push(stack[stack.length - 1] + stack[stack.length - 2]);
        else stack.push(parseInt(op, 10));
    }
    let total = 0;
    for (const value of stack) total += value;
    return total;
}
