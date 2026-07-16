// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

export function verifyPreorder(preorder: number[]): boolean {
    let low = Number.NEGATIVE_INFINITY;
    const stack: number[] = [];

    for (const value of preorder) {
        if (value < low) {
            return false;
        }
        while (stack.length > 0 && stack[stack.length - 1] < value) {
            low = stack.pop()!;
        }
        stack.push(value);
    }

    return true;
}
