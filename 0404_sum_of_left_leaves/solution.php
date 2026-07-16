// LeetCode 0404 - Sum of Left Leaves
// https://leetcode.com/problems/sum-of-left-leaves/

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
     * @param TreeNode|null $root
     * @return Integer
     */
    function sumOfLeftLeaves($root) {
        return $this->sum_of_left_leaves($root);
    }

    /**
     * @param TreeNode|null $root
     * @return Integer
     */
    function sum_of_left_leaves($root) {
        if ($root === null) {
            return 0;
        }

        $total = 0;
        if ($root->left !== null && $root->left->left === null && $root->left->right === null) {
            $total += $root->left->val;
        } else {
            $total += $this->sum_of_left_leaves($root->left);
        }

        $total += $this->sum_of_left_leaves($root->right);
        return $total;
    }
}
