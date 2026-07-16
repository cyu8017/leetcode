<?php
// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution {
    /**
     * @param object|null $root
     * @return Integer[]
     */
    function largestValues($root) {
        return $this->largest_values($root);
    }

    /**
     * @param object|null $root
     * @return Integer[]
     */
    function largest_values($root) {
        if ($root === null) {
            return [];
        }

        $result = [];
        $queue = [$root];

        while (!empty($queue)) {
            $levelMax = PHP_INT_MIN;
            $levelSize = count($queue);
            for ($index = 0; $index < $levelSize; $index++) {
                $node = array_shift($queue);
                $levelMax = max($levelMax, $node->val);
                if ($node->left !== null) {
                    $queue[] = $node->left;
                }
                if ($node->right !== null) {
                    $queue[] = $node->right;
                }
            }
            $result[] = $levelMax;
        }

        return $result;
    }
}
