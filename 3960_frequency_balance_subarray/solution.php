<?php
// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

class Solution {
    function getLength($nums) {
        $n = count($nums);
        $ans = 1;
        for ($l = 0; $l < $n; $l++) {
            $cnt = [];
            $freq = [];
            for ($r = $l; $r < $n; $r++) {
                $x = $nums[$r];
                $c = $cnt[$x] ?? 0;
                if (($freq[$c] ?? 0) > 0) {
                    $fc = $freq[$c] - 1;
                    if ($fc === 0) unset($freq[$c]);
                    else $freq[$c] = $fc;
                }
                $cnt[$x] = $c + 1;
                $cx = $cnt[$x];
                $freq[$cx] = ($freq[$cx] ?? 0) + 1;
                if (count($cnt) === 1 || (count($freq) === 2 && ((($freq[$cx * 2] ?? 0) > 0) || ($cx % 2 === 0 && ($freq[intdiv($cx, 2)] ?? 0) > 0)))) {
                    $ans = max($ans, $r - $l + 1);
                }
            }
        }
        return $ans;
    }
}
