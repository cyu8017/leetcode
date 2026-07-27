<?php
// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

class Solution {
    function lowestCommonAncestor($p, $q) {
        $compatibility = is_array($p) && isset($p["tree"]);
        if ($compatibility) {
            $data = $p;
            $vals = $data["tree"];
            $nodes = [];
            foreach ($vals as $v) {
                $nodes[] = $v === null ? null : (object)["val" => $v, "left" => null, "right" => null, "parent" => null];
            }
            for ($i = 0; $i < count($nodes); $i++) {
                $node = $nodes[$i];
                if ($node === null) continue;
                $leftI = 2 * $i + 1;
                $rightI = 2 * $i + 2;
                if ($leftI < count($nodes) && $nodes[$leftI] !== null) {
                    $node->left = $nodes[$leftI];
                    $nodes[$leftI]->parent = $node;
                }
                if ($rightI < count($nodes) && $nodes[$rightI] !== null) {
                    $node->right = $nodes[$rightI];
                    $nodes[$rightI]->parent = $node;
                }
            }
            $p = null;
            $q = null;
            foreach ($nodes as $x) {
                if ($x !== null && $x->val === $data["p"]) $p = $x;
                if ($x !== null && $x->val === $data["q"]) $q = $x;
            }
        }
        $a = $p;
        $b = $q;
        while ($a !== $b) {
            $a = $a ? $a->parent : $q;
            $b = $b ? $b->parent : $p;
        }
        return $compatibility ? $a->val : $a;
    }
}
