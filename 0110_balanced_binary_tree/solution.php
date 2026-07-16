// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    /**
     * @param TreeNode $root
     * @return Boolean
     */
    function isBalanced($root) {
        return $this->height($root) != -1;
    }

    private function height($node) {
        if ($node === null) {
            return 0;
        }
        $left = $this->height($node->left);
        if ($left == -1) {
            return -1;
        }
        $right = $this->height($node->right);
        if ($right == -1) {
            return -1;
        }
        if (abs($left - $right) > 1) {
            return -1;
        }
        return 1 + max($left, $right);
    }
}
