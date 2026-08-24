<?php
// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

class Solution {
    function findChampion($n, $edges) {
        $indeg = array_fill(0, $n, 0);
        foreach ($edges as $e) $indeg[$e[1]]++;
        $ans = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] === 0) {
                if ($ans !== -1) return -1;
                $ans = $i;
            }
        }
        return $ans;
    }
}
