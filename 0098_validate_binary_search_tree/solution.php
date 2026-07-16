// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

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
    function isValidBST($root) {
        return $this->valid($root, PHP_INT_MIN, PHP_INT_MAX);
    }

    private function valid($node, $low, $high) {
        if ($node === null) {
            return true;
        }
        if (!($low < $node->val && $node->val < $high)) {
            return false;
        }
        return $this->valid($node->left, $low, $node->val)
            && $this->valid($node->right, $node->val, $high);
    }
}
