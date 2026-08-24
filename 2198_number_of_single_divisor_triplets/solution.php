<?php
// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

class Solution {
    function solve($nums) {
        $freq = array_fill(0, 101, 0);
        foreach ($nums as $x) $freq[$x]++;
        $ans = 0;
        for ($a = 1; $a <= 100; $a++) {
            if (!$freq[$a]) continue;
            for ($b = $a; $b <= 100; $b++) {
                if (!$freq[$b]) continue;
                for ($c = $b; $c <= 100; $c++) {
                    if (!$freq[$c]) continue;
                    $s = $a + $b + $c;
                    $cnt = 0;
                    if ($s % $a === 0) $cnt++;
                    if ($s % $b === 0) $cnt++;
                    if ($s % $c === 0) $cnt++;
                    if ($cnt !== 1) continue;
                    if ($a === $b && $b === $c) $ans += $freq[$a] * ($freq[$a] - 1) * ($freq[$a] - 2);
                    else if ($a === $b) $ans += $freq[$a] * ($freq[$a] - 1) * $freq[$c] * 3;
                    else if ($b === $c) $ans += $freq[$b] * ($freq[$b] - 1) * $freq[$a] * 3;
                    else if ($a === $c) $ans += $freq[$a] * ($freq[$a] - 1) * $freq[$b] * 3;
                    else $ans += $freq[$a] * $freq[$b] * $freq[$c] * 6;
                }
            }
        }
        return $ans;
    }
}
