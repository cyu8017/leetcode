// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Node {
    public $val = null;
    /** @var Node[] */
    public $children = [];
    function __construct($val = null, $children = null) {
        $this->val = $val;
        $this->children = $children ?? [];
    }
}

class Solution {
    /**
     * @param Node|null $root
     * @return Integer[][]
     */
    function levelOrder($root) {
        return $this->level_order($root);
    }

    /**
     * @param Node|null $root
     * @return Integer[][]
     */
    function level_order($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $queue = [$root];
        while (count($queue) > 0) {
            $level = [];
            $size = count($queue);
            for ($i = 0; $i < $size; $i++) {
                $node = array_shift($queue);
                $level[] = $node->val;
                foreach ($node->children as $child) {
                    $queue[] = $child;
                }
            }
            $result[] = $level;
        }

        return $result;
    }
}
