<?php
// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $relations
     * @return Integer
     */
    function minimumSemesters($n, $relations) {
        $graph = array_fill(0, $n + 1, []);
        $indeg = array_fill(0, $n + 1, 0);
        foreach ($relations as [$a, $b]) {
            $graph[$a][] = $b;
            $indeg[$b]++;
        }
        $queue = [];
        for ($i = 1; $i <= $n; $i++) {
            if ($indeg[$i] === 0) $queue[] = $i;
        }
        $sem = 0;
        $taken = 0;
        $head = 0;
        while ($head < count($queue)) {
            $sz = count($queue) - $head;
            $sem++;
            for ($i = 0; $i < $sz; $i++) {
                $node = $queue[$head++];
                $taken++;
                foreach ($graph[$node] as $nei) {
                    if (--$indeg[$nei] === 0) $queue[] = $nei;
                }
            }
        }
        return $taken === $n ? $sem : -1;
    }
}
