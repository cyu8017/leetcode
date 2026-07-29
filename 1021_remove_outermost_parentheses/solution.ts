// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

function removeOuterParentheses(s: string): string {
    const ans = [];
    let depth = 0;
    for (const ch of s) {
        if (ch === '(') {
            if (depth) ans.push(ch);
            depth++;
        } else {
            depth--;
            if (depth) ans.push(ch);
        }
    }
    return ans.join('');
}
