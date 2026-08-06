<?php
class Solution {
    function balanceBST($root) {
        $nodes = [];
        $walk = function($x) use (&$walk, &$nodes) {
            if ($x) {
                $walk($x->left);
                $nodes[] = $x;
                $walk($x->right);
            }
        };
        $walk($root);
        $build = function($l, $r) use (&$build, $nodes) {
            if ($l >= $r) return null;
            $m = intdiv($l + $r, 2);
            $x = $nodes[$m];
            $x->left = $build($l, $m);
            $x->right = $build($m + 1, $r);
            return $x;
        };
        return $build(0, count($nodes));
    }
}
