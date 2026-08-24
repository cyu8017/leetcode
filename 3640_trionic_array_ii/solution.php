<?php
// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

class Solution {
    function maxSumTrionic($nums) {
        $n = count($nums);
        $i = 0;
        $ans = -PHP_INT_MAX;
        while ($i < $n) {
            $l = $i;
            for ($i++; $i < $n && $nums[$i - 1] < $nums[$i];) $i++;
            if ($i === $l + 1) continue;
            $p = $i - 1;
            $s = $nums[$p - 1] + $nums[$p];
            while ($i < $n && $nums[$i - 1] > $nums[$i]) {
                $s += $nums[$i];
                $i++;
            }
            if ($i === $p + 1 || $i === $n || $nums[$i - 1] === $nums[$i]) continue;
            $q = $i - 1;
            $s += $nums[$i];
            $i++;
            $mx = 0;
            $t = 0;
            while ($i < $n && $nums[$i - 1] < $nums[$i]) {
                $t += $nums[$i];
                $i++;
                $mx = max($mx, $t);
            }
            $s += $mx;
            $mx = $t = 0;
            for ($j = $p - 2; $j >= $l; $j--) {
                $t += $nums[$j];
                $mx = max($mx, $t);
            }
            $s += $mx;
            $ans = max($ans, $s);
            $i = $q;
        }
        return $ans;
    }
}
