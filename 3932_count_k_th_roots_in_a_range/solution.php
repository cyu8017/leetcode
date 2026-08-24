<?php
// LeetCode 3932 - Count K Th Roots In A Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/

class Solution {
    function countKthRoots($l, $r, $k) {
        if ($k == 1) return $r - $l + 1;
        $ans = 0;
        for ($x = 0; ; $x++) {
            $y = 1;
            $tooBig = false;
            for ($i = 0; $i < $k; $i++) {
                if ($x != 0 && $y > intdiv($r, $x)) {
                    $tooBig = true;
                    break;
                }
                $y *= $x;
                if ($y > $r) break;
            }
            if ($tooBig || $y > $r) break;
            if ($l <= $y && $y <= $r) $ans++;
        }
        return $ans;
    }
}
