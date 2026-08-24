// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

function isContiguous(a: any, b: any): any {
    const x = Math.abs(a.charCodeAt(0) - b.charCodeAt(0));
    return x === 1 || x === 25;
}export function resultingString(s: any): any {
    const stk = [];
    for (const c of s) {
        if (stk.length > 0 && isContiguous(stk[stk.length - 1], c))
            stk.pop();
        else stk.push(c);
    }
    return stk.join('');
}
