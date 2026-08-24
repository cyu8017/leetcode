<?php
// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

class Solution {
    function uniqueMode($a) {
        $freq = [];
        foreach ($a as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $best = 0;
        $cnt = 0;
        foreach ($freq as $f) {
            if ($f > $best) { $best = $f; $cnt = 1; }
            else if ($f === $best) $cnt++;
        }
        return $cnt === 1;
    }

    function subsequencesWithMiddleMode($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $ans = 0;
        for ($mid = 2; $mid < $n - 2; $mid++) {
            for ($a = 0; $a < $mid; $a++) {
                for ($b = $a + 1; $b < $mid; $b++) {
                    for ($c = $mid + 1; $c < $n; $c++) {
                        for ($d = $c + 1; $d < $n; $d++) {
                            if ($this->uniqueMode([$nums[$a], $nums[$b], $nums[$mid], $nums[$c], $nums[$d]])) $ans++;
                        }
                    }
                }
            }
        }
        return $ans % $mod;
    }
}
