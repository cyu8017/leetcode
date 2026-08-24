<?php
// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

class Solution {
    function getResults($nums, $queries) {
        $a = $nums;
        $ans = [];
        foreach ($queries as $q) {
            $typ = $q[0];
            if ($typ === 1) {
                $l = $q[1];
                $r = $q[2];
                while ($l < $r) {
                    $tmp = $a[$l];
                    $a[$l] = $a[$r];
                    $a[$r] = $tmp;
                    $l++;
                    $r--;
                }
            } else if ($typ === 2) {
                $x = 0;
                for ($i = $q[1]; $i <= $q[2]; $i++) $x ^= $a[$i];
                $ans[] = $x;
            } else {
                $a[$q[1]] = $q[2];
            }
        }
        return $ans;
    }
}
