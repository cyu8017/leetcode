// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

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
     * @return Integer
     */
    function countNodes($root) {
        if ($root === null) {
            return 0;
        }
        $left = $this->leftDepth($root);
        $right = $this->rightDepth($root);
        if ($left === $right) {
            return (1 << $left) - 1;
        }
        return 1 + $this->countNodes($root->left) + $this->countNodes($root->right);
    }

    private function leftDepth($node) {
        $depth = 0;
        while ($node !== null) {
            $depth++;
            $node = $node->left;
        }
        return $depth;
    }

    private function rightDepth($node) {
        $depth = 0;
        while ($node !== null) {
            $depth++;
            $node = $node->right;
        }
        return $depth;
    }
}
