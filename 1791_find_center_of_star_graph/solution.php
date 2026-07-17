<?php
// LeetCode 1791 - Find Center of Star Graph
// https://leetcode.com/problems/find-center-of-star-graph/

class Solution {
    /**
     * @param Integer[][] $edges
     * @return Integer
     */
    function findCenter($edges) {
        list($a, $b) = $edges[0];
        list($c, $d) = $edges[1];
        return ($a === $c || $a === $d) ? $a : $b;
    }
}
