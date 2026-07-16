// LeetCode 0103 - Binary Tree Zigzag Level Order Traversal
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

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
    function zigzagLevelOrder($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $queue = [$root];
        $leftToRight = true;

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
            if (!$leftToRight) {
                $level = array_reverse($level);
            }
            $result[] = $level;
            $leftToRight = !$leftToRight;
        }

        return $result;
    }
}
