<?php
// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Boolean
     */
    function validTree($n, $edges) {
        if (count($edges) !== $n - 1) {
            return false;
        }
        $parent = range(0, $n - 1);
        $find = function($node) use (&$parent, &$find) {
            if ($parent[$node] !== $node) {
                $parent[$node] = $find($parent[$node]);
            }
            return $parent[$node];
        };
        foreach ($edges as $edge) {
            $rootLeft = $find($edge[0]);
            $rootRight = $find($edge[1]);
            if ($rootLeft === $rootRight) {
                return false;
            }
            $parent[$rootLeft] = $rootRight;
        }
        return true;
    }
}
