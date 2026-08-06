<?php
// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class Solution {
    /**
     * @param TreeNode $root
     * @return Integer
     */
    function maxLevelSum($root) {
        $queue = [$root];
        $bestSum = PHP_INT_MIN;
        $bestLevel = $level = 1;
        $head = 0;
        while ($head < count($queue)) {
            $sz = count($queue) - $head;
            $total = 0;
            for ($i = 0; $i < $sz; $i++) {
                $node = $queue[$head++];
                $total += $node->val;
                if ($node->left !== null) $queue[] = $node->left;
                if ($node->right !== null) $queue[] = $node->right;
            }
            if ($total > $bestSum) {
                $bestSum = $total;
                $bestLevel = $level;
            }
            $level++;
        }
        return $bestLevel;
    }
}
