<?php
// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

class Solution {
    /**
     * @param TreeNode $root
     * @param Integer[] $to_delete
     * @return TreeNode[]
     */
    function delNodes($root, $to_delete) {
        $delete = array_flip($to_delete);
        $forest = [];
        $dfs = function ($node, $isRoot) use (&$dfs, &$delete, &$forest) {
            if ($node === null) return null;
            $removed = isset($delete[$node->val]);
            if ($isRoot && !$removed) $forest[] = $node;
            $node->left = $dfs($node->left, $removed);
            $node->right = $dfs($node->right, $removed);
            return $removed ? null : $node;
        };
        $dfs($root, true);
        return $forest;
    }
}
