<?php
// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution {
    function queryResults($limit, $queries) {
        $g = [];
        $cnt = [];
        $ans = [];
        $ai = 0;
        foreach ($queries as $q) {
            $x = $q[0];
            $y = $q[1];
            $cnt[$y] = ($cnt[$y] ?? 0) + 1;
            if (isset($g[$x])) {
                $old = $g[$x];
                $nv = $cnt[$old] - 1;
                if ($nv === 0) unset($cnt[$old]);
                else $cnt[$old] = $nv;
            }
            $g[$x] = $y;
            $ans[$ai++] = count($cnt);
        }
        return $ans;
    }
}
