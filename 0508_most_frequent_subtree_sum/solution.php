<?php
// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

class Solution {
    /**
     * @param object|null $root
     * @return Integer[]
     */
    function findFrequentTreeSum($root) {
        return $this->find_frequent_tree_sum($root);
    }

    /**
     * @param object|null $root
     * @return Integer[]
     */
    function find_frequent_tree_sum($root) {
        $counts = [];

        $subtreeSum = function ($node) use (&$subtreeSum, &$counts) {
            if ($node === null) {
                return 0;
            }
            $total = $node->val + $subtreeSum($node->left) + $subtreeSum($node->right);
            $counts[$total] = ($counts[$total] ?? 0) + 1;
            return $total;
        };

        $subtreeSum($root);
        if ($counts === []) {
            return [];
        }
        $best = max($counts);
        $result = [];
        foreach ($counts as $value => $count) {
            if ($count === $best) {
                $result[] = $value;
            }
        }
        sort($result);
        return $result;
    }
}
