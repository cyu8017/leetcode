<?php
// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

class Solution {
    function leastOpsExpressTarget($x, $target) {
        $memo = [];
        $dfs = function ($t) use (&$dfs, &$memo, $x) {
            if (array_key_exists($t, $memo)) return $memo[$t];
            if ($x > $t) {
                $ans = min(2 * $t - 1, 2 * ($x - $t));
                $memo[$t] = $ans;
                return $ans;
            }
            if ($x === $t) {
                $memo[$t] = 0;
                return 0;
            }
            $prod = $x;
            $n = 0;
            while ($prod < $t) {
                $prod *= $x;
                $n++;
            }
            if ($prod === $t) {
                $memo[$t] = $n;
                return $n;
            }
            $ans = $dfs($t - intdiv($prod, $x)) + $n;
            if ($prod < 2 * $t) $ans = min($ans, $dfs($prod - $t) + $n + 1);
            $memo[$t] = $ans;
            return $ans;
        };
        return $dfs($target);
    }
}
