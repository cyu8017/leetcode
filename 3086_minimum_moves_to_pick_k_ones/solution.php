<?php
// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

class Solution {
    function minimumMoves($nums, $k, $maxChanges) {
        $n = count($nums);
        $cnt = array_fill(0, $n + 1, 0);
        $s = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $cnt[$i] = $cnt[$i - 1] + $nums[$i - 1];
            $s[$i] = $s[$i - 1] + $i * $nums[$i - 1];
        }
        $ans = PHP_INT_MAX;
        for ($i = 1; $i <= $n; $i++) {
            $t = 0;
            $need = $k - $nums[$i - 1];
            foreach ([$i - 1, $i + 1] as $j) {
                if ($need > 0 && 1 <= $j && $j <= $n && $nums[$j - 1] === 1) {
                    $need--;
                    $t++;
                }
            }
            $c = min($need, $maxChanges);
            $need -= $c;
            $t += $c * 2;
            if ($need <= 0) {
                $ans = min($ans, $t);
                continue;
            }
            $l = 2;
            $r = max($i - 1, $n - $i);
            while ($l <= $r) {
                $mid = ($l + $r) >> 1;
                $l1 = max(1, $i - $mid);
                $r1 = max(0, $i - 2);
                $l2 = min($n + 1, $i + 2);
                $r2 = min($n, $i + $mid);
                $c1 = $cnt[$r1] - $cnt[$l1 - 1];
                $c2 = $cnt[$r2] - $cnt[$l2 - 1];
                if ($c1 + $c2 >= $need) {
                    $t1 = $c1 * $i - ($s[$r1] - $s[$l1 - 1]);
                    $t2 = $s[$r2] - $s[$l2 - 1] - $c2 * $i;
                    $ans = min($ans, $t + $t1 + $t2);
                    $r = $mid - 1;
                } else {
                    $l = $mid + 1;
                }
            }
        }
        return $ans;
    }
}
