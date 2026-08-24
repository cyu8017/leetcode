<?php
// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

class Solution {
    function tryCand(&$ndp, $base, $na, $nb, $v) {
        if ($base + $v < $ndp[$na][$nb]) $ndp[$na][$nb] = $base + $v;
    }

    function minArraySum($nums, $k, $op1, $op2) {
        $inf = 1e18;
        $dp = [];
        for ($a = 0; $a <= $op1; $a++) $dp[$a] = array_fill(0, $op2 + 1, $inf);
        $dp[0][0] = 0;
        foreach ($nums as $x) {
            $ndp = [];
            for ($a = 0; $a <= $op1; $a++) $ndp[$a] = array_fill(0, $op2 + 1, $inf);
            for ($a = 0; $a <= $op1; $a++) {
                for ($b = 0; $b <= $op2; $b++) {
                    if ($dp[$a][$b] === $inf) continue;
                    $this->tryCand($ndp, $dp[$a][$b], $a, $b, $x);
                    if ($a < $op1) $this->tryCand($ndp, $dp[$a][$b], $a + 1, $b, intdiv($x + 1, 2));
                    if ($b < $op2 && $x >= $k) $this->tryCand($ndp, $dp[$a][$b], $a, $b + 1, $x - $k);
                    if ($a < $op1 && $b < $op2) {
                        $v1 = intdiv($x + 1, 2);
                        if ($v1 >= $k) $this->tryCand($ndp, $dp[$a][$b], $a + 1, $b + 1, $v1 - $k);
                        if ($x >= $k) $this->tryCand($ndp, $dp[$a][$b], $a + 1, $b + 1, intdiv($x - $k + 1, 2));
                    }
                }
            }
            $dp = $ndp;
        }
        $ans = $inf;
        for ($a = 0; $a <= $op1; $a++)
            for ($b = 0; $b <= $op2; $b++)
                if ($dp[$a][$b] < $ans) $ans = $dp[$a][$b];
        return $ans;
    }
}
