<?php
// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

class Solution {
    function popcountDepth($nums, $queries) {
        $bitCount = function($x) {
            $c = 0;
            $v = $x;
            while ($v) { $c += $v & 1; $v >>= 1; }
            return $c;
        };
        $depth = function($x) use ($bitCount) {
            $v = $x;
            if ($v === 1) return 0;
            $d = 0;
            while ($v > 1) {
                $v = $bitCount($v);
                $d++;
            }
            return $d;
        };
        $a = $nums;
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $l = $q[1];
                $r = $q[2];
                $k = $q[3];
                $cnt = 0;
                for ($i = $l; $i <= $r; $i++)
                    if ($depth($a[$i]) === $k) $cnt++;
                $ans[] = $cnt;
            } else {
                $a[$q[1]] = $q[2];
            }
        }
        return $ans;
    }
}
