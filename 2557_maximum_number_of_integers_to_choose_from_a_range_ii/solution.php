<?php
// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

class Solution {
    function maxCount($banned, $n, $maxSum) {
        sort($banned);
        $uniq = [];
        foreach ($banned as $x) {
            if ($x >= 1 && $x <= $n && (!$uniq || $uniq[count($uniq) - 1] !== $x)) $uniq[] = $x;
        }
        $ans = 0;
        $remain = $maxSum;
        $prev = 0;
        $check = function($l, $r) use (&$ans, &$remain) {
            if ($l > $r || $remain <= 0) return;
            $lo = $l;
            $hi = $r;
            $best = $l - 1;
            while ($lo <= $hi) {
                $mid = intdiv($lo + $hi, 2);
                $cnt = $mid - $l + 1;
                $sum = intdiv(($l + $mid) * $cnt, 2);
                if ($sum <= $remain) {
                    $best = $mid;
                    $lo = $mid + 1;
                } else $hi = $mid - 1;
            }
            if ($best >= $l) {
                $cnt = $best - $l + 1;
                $ans += $cnt;
                $remain -= intdiv(($l + $best) * $cnt, 2);
            }
        };
        foreach ($uniq as $b) {
            $check($prev + 1, $b - 1);
            $prev = $b;
        }
        $check($prev + 1, $n);
        return $ans;
    }
}
