// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    function isValid(text) {
        let balance = 0;
        for (const char of text) {
            if (char === "(") {
                balance += 1;
            } else if (char === ")") {
                if (balance === 0) {
                    return false;
                }
                balance -= 1;
            }
        }
        return balance === 0;
    }

    const result = new Set();
    const queue = [s];
    const visited = new Set([s]);
    let found = false;
    while (queue.length > 0) {
        const levelSize = queue.length;
        for (let step = 0; step < levelSize; step += 1) {
            const current = queue.shift();
            if (isValid(current)) {
                result.add(current);
                found = true;
            }
            if (found) {
                continue;
            }
            for (let index = 0; index < current.length; index += 1) {
                if (current[index] !== "(" && current[index] !== ")") {
                    continue;
                }
                const nxt = current.slice(0, index) + current.slice(index + 1);
                if (!visited.has(nxt)) {
                    visited.add(nxt);
                    queue.push(nxt);
                }
            }
        }
    }
    return [...result];
};
