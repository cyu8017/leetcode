// LeetCode 0404 - Sum of Left Leaves
type TreeNode = { val: number; left: TreeNode | null; right: TreeNode | null };

export function sumOfLeftLeaves(root: TreeNode | null): number {
    if (!root) return 0;
    let total = 0;
    if (root.left && !root.left.left && !root.left.right) {
        total += root.left.val;
    } else {
        total += sumOfLeftLeaves(root.left);
    }
    total += sumOfLeftLeaves(root.right);
    return total;
}
