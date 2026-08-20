// LeetCode 1325 - Delete Leaves With A Given Value
// https://leetcode.com/problems/delete-leaves-with-a-given-value/

function removeLeafNodes(root: any, target: number): any {
    if (!root) return null;
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    if (!root.left && !root.right && root.val === target) return null;
    return root;
}
