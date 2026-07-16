// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

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
     * @param Integer[] $nums
     * @return TreeNode
     */
    function sortedArrayToBST($nums) {
        return $this->build($nums, 0, count($nums) - 1);
    }

    private function build($nums, $left, $right) {
        if ($left > $right) {
            return null;
        }
        $mid = intdiv($left + $right + 1, 2);
        $root = new TreeNode($nums[$mid]);
        $root->left = $this->build($nums, $left, $mid - 1);
        $root->right = $this->build($nums, $mid + 1, $right);
        return $root;
    }
}
