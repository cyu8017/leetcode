// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

function interpret(command: string): string {
    return command.replace(/\(\)/g, "o").replace(/\(al\)/g, "al");
}
