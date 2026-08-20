"use strict";
// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/
function isSolvable(words, result) {
    if (Math.max(...words.map((w) => w.length)) > result.length)
        return false;
    const letters = new Set((words.join("") + result).split(""));
    if (letters.size > 10)
        return false;
    const leading = new Set();
    for (const word of [...words, result]) {
        if (word.length > 1)
            leading.add(word[0]);
    }
    const value = new Map();
    const used = Array(10).fill(false);
    const width = result.length;
    const solve = (column, row, total) => {
        if (column === width)
            return total === 0;
        if (row < words.length) {
            if (column >= words[row].length)
                return solve(column, row + 1, total);
            const ch = words[row][words[row].length - 1 - column];
            if (value.has(ch))
                return solve(column, row + 1, total + value.get(ch));
            for (let digit = 0; digit < 10; digit++) {
                if (!used[digit] && (digit || !leading.has(ch))) {
                    value.set(ch, digit);
                    used[digit] = true;
                    if (solve(column, row + 1, total + digit))
                        return true;
                    used[digit] = false;
                    value.delete(ch);
                }
            }
            return false;
        }
        const ch = result[result.length - 1 - column];
        const digit = total % 10;
        const carry = Math.floor(total / 10);
        if (value.has(ch))
            return value.get(ch) === digit && solve(column + 1, 0, carry);
        if (used[digit] || (digit === 0 && leading.has(ch)))
            return false;
        value.set(ch, digit);
        used[digit] = true;
        const ok = solve(column + 1, 0, carry);
        used[digit] = false;
        value.delete(ch);
        return ok;
    };
    return solve(0, 0, 0);
}
