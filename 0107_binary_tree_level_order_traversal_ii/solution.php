// LeetCode 0107 - Binary Tree Level Order Traversal II
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

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
     * @return Integer[][]
     */
    function levelOrderBottom($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $queue = [$root];

        while (!empty($queue)) {
            $size = count($queue);
            $level = [];
            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);
                $level[] = $node->val;
                if ($node->left !== null) {
                    $queue[] = $node->left;
                }
                if ($node->right !== null) {
                    $queue[] = $node->right;
                }
            }
            $result[] = $level;
        }

        return array_reverse($result);
    }
}
