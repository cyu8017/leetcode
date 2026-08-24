<?php
// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

class Solution {
    function removeSubstring($s, $k) {
        $stk = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $sn = count($stk);
            if ($sn && $stk[$sn - 1][0] === $c)
                $stk[$sn - 1][1]++;
            else $stk[] = [$c, 1];
            $sn = count($stk);
            if ($c === ')' && $sn > 1) {
                $top = $stk[$sn - 1];
                if ($top[1] === $k && $stk[$sn - 2][1] >= $k) {
                    array_pop($stk);
                    $stk[$sn - 2][1] -= $k;
                    if ($stk[$sn - 2][1] === 0) array_pop($stk);
                }
            }
        }
        $res = '';
        foreach ($stk as $p)
            for ($i = 0; $i < $p[1]; $i++) $res .= $p[0];
        return $res;
    }
}
