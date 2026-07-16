// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

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
     * @param TreeNode $p
     * @return TreeNode|null
     */
    function inorderSuccessor($root, $p) {
        if ($p->right !== null) {
            $current = $p->right;
            while ($current->left !== null) {
                $current = $current->left;
            }
            return $current;
        }
        $successor = null;
        $current = $root;
        while ($current !== null) {
            if ($p->val < $current->val) {
                $successor = $current;
                $current = $current->left;
            } else {
                $current = $current->right;
            }
        }
        return $successor;
    }
}
