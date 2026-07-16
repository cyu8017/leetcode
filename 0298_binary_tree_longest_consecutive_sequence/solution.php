// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

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
    function longestConsecutive($root) {
        $dfs = function ($node, $parent, $length) use (&$dfs) {
            if ($node === null) {
                return 0;
            }
            $current = ($parent !== null && $parent->val + 1 === $node->val) ? $length + 1 : 1;
            return max(
                $current,
                $dfs($node->left, $node, $current),
                $dfs($node->right, $node, $current)
            );
        };
        return $dfs($root, null, 0);
    }
}
