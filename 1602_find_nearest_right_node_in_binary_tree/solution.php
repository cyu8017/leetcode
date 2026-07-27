<?php
// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

class Solution {
    /**
     * @param TreeNode $root
     * @param TreeNode|Integer $u
     * @return TreeNode|Integer|null
     */
    function findNearestRightNode($root, $u) {
        $asNode = is_object($u) && property_exists($u, 'val');
        $target = $asNode ? $u->val : $u;
        $q = $root ? [$root] : [];
        while ($q) {
            $nxt = [];
            $n = count($q);
            for ($i = 0; $i < $n; $i++) {
                $node = $q[$i];
                if ($node->val === $target) {
                    $ans = $i + 1 < $n ? $q[$i + 1] : null;
                    return $asNode ? $ans : ($ans ? $ans->val : null);
                }
                if ($node->left) {
                    $nxt[] = $node->left;
                }
                if ($node->right) {
                    $nxt[] = $node->right;
                }
            }
            $q = $nxt;
        }
        return null;
    }
}
