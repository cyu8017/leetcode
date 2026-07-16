// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

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
     * @return NULL
     */
    function recoverTree($root) {
        $first = null;
        $second = null;
        $previous = null;
        $stack = [];
        $current = $root;

        while ($current !== null || count($stack) > 0) {
            while ($current !== null) {
                $stack[] = $current;
                $current = $current->left;
            }
            $current = array_pop($stack);
            if ($previous !== null && $previous->val > $current->val) {
                if ($first === null) {
                    $first = $previous;
                }
                $second = $current;
            }
            $previous = $current;
            $current = $current->right;
        }

        if ($first !== null && $second !== null) {
            $temp = $first->val;
            $first->val = $second->val;
            $second->val = $temp;
        }
    }
}
