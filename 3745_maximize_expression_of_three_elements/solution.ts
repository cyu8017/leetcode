// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

export function maximizeExpressionOfThree(nums: any): any {
    const inf = 1 << 30;
    let a = -inf, b = -inf, c = inf;
    for (const x of nums) {
        if (x < c) c = x;
        if (x >= a) { b = a; a = x; }
        else if (x > b) b = x;
    }
    return a + b - c;
}
