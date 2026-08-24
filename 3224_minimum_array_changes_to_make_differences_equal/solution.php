<?php
// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

class Solution {
    function minChanges($nums, $k) {
        $d = array_fill(0, $k + 2, 0);
        $n = count($nums);
        for ($i = 0; $i * 2 < $n; $i++) {
            $x = $nums[$i];
            $y = $nums[$n - 1 - $i];
            if ($x > $y) { $t = $x; $x = $y; $y = $t; }
            $d[0] += 1;
            $d[$y - $x] -= 1;
            $d[$y - $x + 1] += 1;
            $mx = max($y, $k - $x);
            $d[$mx + 1] -= 1;
            $d[$mx + 1] += 2;
        }
        $ans = $n;
        $s = 0;
        foreach ($d as $x) {
            $s += $x;
            $ans = min($ans, $s);
        }
        return $ans;
    }
}
