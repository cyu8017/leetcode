<?php
// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

class Solution {
    /**
     * @param object|null $root
     * @return Integer[]
     */
    function findMode($root) {
        return $this->find_mode($root);
    }

    /**
     * @param object|null $root
     * @return Integer[]
     */
    function find_mode($root) {
        $counts = [];
        $best = 0;

        $inorder = function ($node) use (&$inorder, &$counts, &$best) {
            if ($node === null) {
                return;
            }
            $inorder($node->left);
            $value = $node->val;
            $counts[$value] = ($counts[$value] ?? 0) + 1;
            $best = max($best, $counts[$value]);
            $inorder($node->right);
        };

        $inorder($root);
        $result = [];
        foreach ($counts as $value => $count) {
            if ($count === $best) {
                $result[] = $value;
            }
        }
        return $result;
    }
}
