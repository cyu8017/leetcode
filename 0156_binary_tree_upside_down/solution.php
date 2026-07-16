// LeetCode 0156 - Binary Tree Upside Down
// https://leetcode.com/problems/binary-tree-upside-down/

class TreeNode {
    public int $val;
    public ?TreeNode $left;
    public ?TreeNode $right;

    function __construct(int $val = 0, ?TreeNode $left = null, ?TreeNode $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    function upsideDownBinaryTree(?TreeNode $root): ?TreeNode {
        $previous = null;
        $previousRight = null;
        $current = $root;
        while ($current !== null) {
            $next = $current->left;
            $current->left = $previousRight;
            $previousRight = $current->right;
            $current->right = $previous;
            $previous = $current;
            $current = $next;
        }
        return $previous;
    }
}