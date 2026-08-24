<?php
// LeetCode 3095 - Shortest Subarray With OR at Least K I
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

class Solution {
    function minimumSubarrayLength($nums, $k) {
        $n = count($nums);
        $cnt = array_fill(0, 32, 0);
        $ans = $n + 1;
        $s = 0;
        $i = 0;
        for ($j = 0; $j < $n; $j++) {
            $x = $nums[$j];
            $s |= $x;
            for ($h = 0; $h < 32; $h++)
                if ((($x >> $h) & 1) !== 0) $cnt[$h]++;
            for (; $s >= $k && $i <= $j; $i++) {
                $ans = min($ans, $j - $i + 1);
                for ($h = 0; $h < 32; $h++) {
                    if ((($nums[$i] >> $h) & 1) !== 0) {
                        $cnt[$h]--;
                        if ($cnt[$h] === 0) $s ^= 1 << $h;
                    }
                }
            }
        }
        return $ans === $n + 1 ? -1 : $ans;
    }
}
