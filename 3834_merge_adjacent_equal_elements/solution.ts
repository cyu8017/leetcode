// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge_adjacent_equal_elements/

export function mergeAdjacent(nums: any): any {
    const stk = [];
    for (const x of nums) {
        stk.push(x);
        while (stk.length > 1 && stk[stk.length - 1] === stk[stk.length - 2]) {
            const a = stk.pop();
            const b = stk.pop();
            stk.push(a + b);
        }
    }
    return stk;
}
