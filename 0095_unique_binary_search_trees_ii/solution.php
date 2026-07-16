// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

class TreeNode {
    public $val = null;
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
     * @param Integer $n
     * @return TreeNode[]
     */
    function generateTrees($n) {
        if ($n === 0) {
            return [];
        }
        return $this->build(1, $n);
    }

    private function build($start, $end) {
        if ($start > $end) {
            return [null];
        }
        $trees = [];
        for ($rootVal = $start; $rootVal <= $end; $rootVal++) {
            $leftTrees = $this->build($start, $rootVal - 1);
            $rightTrees = $this->build($rootVal + 1, $end);
            foreach ($leftTrees as $left) {
                foreach ($rightTrees as $right) {
                    $trees[] = new TreeNode($rootVal, $left, $right);
                }
            }
        }
        return $trees;
    }
}
