<?php
// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

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
     * @param Node $root
     * @param Node $p
     * @param Node $q
     * @return Node
     */
    function moveSubTree($root, $p, $q) {
        $parent = new SplObjectStorage();

        $build = function ($node) use (&$build, $parent) {
            foreach ($node->children as $child) {
                $parent[$child] = $node;
                $build($child);
            }
        };
        $build($root);

        if ($parent->contains($p) && $parent[$p] === $q) {
            return $root;
        }

        $isAncestor = function ($a, $b) use ($parent) {
            $cur = $b;
            while ($parent->contains($cur)) {
                $cur = $parent[$cur];
                if ($cur === $a) {
                    return true;
                }
            }
            return false;
        };

        $pParent = $parent->contains($p) ? $parent[$p] : null;
        $qParent = $parent->contains($q) ? $parent[$q] : null;

        if ($isAncestor($p, $q)) {
            $idx = array_search($q, $qParent->children, true);
            array_splice($qParent->children, $idx, 1);
            if ($pParent === null) {
                $root = $q;
            } else {
                $pIdx = array_search($p, $pParent->children, true);
                $pParent->children[$pIdx] = $q;
            }
            $q->children[] = $p;
        } else {
            if ($pParent === null) {
                $root = $q;
            } else {
                $idx = array_search($p, $pParent->children, true);
                array_splice($pParent->children, $idx, 1);
            }
            $q->children[] = $p;
        }

        return $root;
    }
}
