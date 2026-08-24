<?php
// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

class Solution {
    function xorAfterQueries($nums, $queries) {
        $mod = 1000000007;
        foreach ($queries as $q) {
            $l = $q[0];
            $r = $q[1];
            $k = $q[2];
            $v = $q[3];
            for ($idx = $l; $idx <= $r; $idx += $k)
                $nums[$idx] = ($nums[$idx] * $v) % $mod;
        }
        $ans = 0;
        foreach ($nums as $x) $ans ^= $x;
        return $ans;
    }
}
