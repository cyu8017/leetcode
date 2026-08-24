<?php
// LeetCode 3919 - Minimum Cost to Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

class Solution {
    function minCost($nums, $queries) {
        $n = count($nums);
        $s1 = array_fill(0, $n, 0);
        $s2 = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            $c1 = 1;
            if ($i > 1 && $nums[$i - 1] - $nums[$i - 2] <= $nums[$i] - $nums[$i - 1]) $c1 = $nums[$i] - $nums[$i - 1];
            $c2 = 1;
            if ($i < $n - 1 && $nums[$i] - $nums[$i - 1] > $nums[$i + 1] - $nums[$i]) $c2 = $nums[$i] - $nums[$i - 1];
            $s1[$i] = $s1[$i - 1] + $c1;
            $s2[$i] = $s2[$i - 1] + $c2;
        }
        $ans = [];
        $qn = count($queries);
        for ($i = 0; $i < $qn; $i++) {
            $l = $queries[$i][0];
            $r = $queries[$i][1];
            $ans[$i] = ($l < $r) ? ($s1[$r] - $s1[$l]) : ($s2[$l] - $s2[$r]);
        }
        return $ans;
    }
}
