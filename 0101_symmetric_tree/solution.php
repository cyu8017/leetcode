// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

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
    function isSymmetric($root) {
        if ($root === null) {
            return true;
        }
        return $this->mirrors($root->left, $root->right);
    }

    /**
     * @param TreeNode $left
     * @param TreeNode $right
     * @return Boolean
     */
    private function mirrors($left, $right) {
        if ($left === null && $right === null) {
            return true;
        }
        if ($left === null || $right === null || $left->val !== $right->val) {
            return false;
        }
        return $this->mirrors($left->left, $right->right) && $this->mirrors($left->right, $right->left);
    }
}
