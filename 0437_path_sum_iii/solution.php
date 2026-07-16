// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

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
    /** @var array<int, int> */
    private $prefixCounts = [];

    /**
     * @param TreeNode|null $root
     * @param int $targetSum
     * @return int
     */
    function pathSum($root, $targetSum) {
        return $this->path_sum($root, $targetSum);
    }

    /**
     * @param TreeNode|null $root
     * @param int $targetSum
     * @return int
     */
    function path_sum($root, $targetSum) {
        $this->prefixCounts = [0 => 1];
        return $this->dfs($root, 0, $targetSum);
    }

    /**
     * @param TreeNode|null $node
     * @param int $current
     * @param int $targetSum
     * @return int
     */
    private function dfs($node, $current, $targetSum) {
        if ($node === null) {
            return 0;
        }

        $current += $node->val;
        $total = $this->prefixCounts[$current - $targetSum] ?? 0;
        $this->prefixCounts[$current] = ($this->prefixCounts[$current] ?? 0) + 1;
        $total += $this->dfs($node->left, $current, $targetSum);
        $total += $this->dfs($node->right, $current, $targetSum);
        $this->prefixCounts[$current]--;
        return $total;
    }
}
