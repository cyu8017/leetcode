<?php
// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $relations
     * @param Integer[] $time
     * @return Integer
     */
    function minimumTime($n, $relations, $time) {
        $g = array_fill(0, $n + 1, []);
        $indeg = array_fill(0, $n + 1, 0);
        $dist = array_fill(0, $n + 1, 0);
        foreach ($relations as $e) { $g[$e[0]][] = $e[1]; $indeg[$e[1]]++; }
        $q = [];
        for ($i = 1; $i <= $n; $i++) {
            $dist[$i] = $time[$i - 1];
            if ($indeg[$i] === 0) $q[] = $i;
        }
        while ($q) {
            $u = array_shift($q);
            foreach ($g[$u] as $v) {
                $dist[$v] = max($dist[$v], $dist[$u] + $time[$v - 1]);
                if (--$indeg[$v] === 0) $q[] = $v;
            }
        }
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) $ans = max($ans, $dist[$i]);
        return $ans;
    }
}
