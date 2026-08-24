<?php
// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

class Solution {
    function maxFrequency($nums, $k) {
        $base = 0;
        foreach ($nums as $x) if ($x === $k) $base++;
        $ans = $base;
        $uniq = [];
        foreach ($nums as $x) $uniq[$x] = true;
        foreach ($uniq as $v => $_) {
            if ($v === $k) continue;
            $best = 0;
            $cur = 0;
            foreach ($nums as $x) {
                $delta = 0;
                if ($x === $v) $delta = 1;
                else if ($x === $k) $delta = -1;
                $cur += $delta;
                if ($cur < 0) $cur = 0;
                if ($cur > $best) $best = $cur;
            }
            if ($base + $best > $ans) $ans = $base + $best;
        }
        return $ans;
    }
}
