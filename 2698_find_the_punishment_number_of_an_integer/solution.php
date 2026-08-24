<?php
// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution {
    function punishmentNumber($n) {
        $dfs = function($s, $i, $sum, $target) use (&$dfs) {
            if ($i === strlen($s)) return $sum === $target;
            $cur = 0;
            for ($j = $i; $j < strlen($s); $j++) {
                $cur = $cur * 10 + (ord($s[$j]) - 48);
                if ($sum + $cur > $target) break;
                if ($dfs($s, $j + 1, $sum + $cur, $target)) return true;
            }
            return false;
        };
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) {
            $sq = $i * $i;
            if ($dfs((string)$sq, 0, 0, $i)) $ans += $sq;
        }
        return $ans;
    }
}
