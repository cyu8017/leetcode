<?php
// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $source
     * @param Integer $destination
     * @return Boolean
     */
    function validPath($n, $edges, $source, $destination) {
        if ($source === $destination) {
            return true;
        }
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $stack = [$source];
        $seen = [$source => true];
        while (!empty($stack)) {
            $u = array_pop($stack);
            if ($u === $destination) {
                return true;
            }
            foreach ($g[$u] as $v) {
                if (!isset($seen[$v])) {
                    $seen[$v] = true;
                    $stack[] = $v;
                }
            }
        }
        return false;
    }
}
