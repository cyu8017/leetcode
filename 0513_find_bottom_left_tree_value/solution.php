<?php
// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution {
    /**
     * @param object|null $root
     * @return Integer
     */
    function findBottomLeftValue($root) {
        return $this->find_bottom_left_value($root);
    }

    /**
     * @param object|null $root
     * @return Integer
     */
    function find_bottom_left_value($root) {
        if ($root === null) {
            return 0;
        }

        $queue = [$root];
        $leftmost = $root->val;

        while (!empty($queue)) {
            $levelSize = count($queue);
            for ($index = 0; $index < $levelSize; $index++) {
                $node = array_shift($queue);
                if ($index === 0) {
                    $leftmost = $node->val;
                }
                if ($node->left !== null) {
                    $queue[] = $node->left;
                }
                if ($node->right !== null) {
                    $queue[] = $node->right;
                }
            }
        }

        return $leftmost;
    }
}
