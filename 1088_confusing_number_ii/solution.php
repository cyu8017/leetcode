<?php
// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function confusingNumberII($n) {
        $rotate = [0 => 0, 1 => 1, 6 => 9, 8 => 8, 9 => 6];
        $digits = [0, 1, 6, 8, 9];
        $ans = 0;
        $isConfusing = function ($num) use ($rotate) {
            $original = $num;
            $rotated = 0;
            while ($num) {
                $d = $num % 10;
                $rotated = $rotated * 10 + $rotate[$d];
                $num = intdiv($num, 10);
            }
            return $rotated !== $original;
        };
        $dfs = null;
        $dfs = function ($cur) use (&$dfs, &$ans, $n, $digits, $isConfusing) {
            if ($cur > $n) {
                return;
            }
            if ($cur && $isConfusing($cur)) {
                $ans++;
            }
            if ($cur === 0) {
                foreach ([1, 6, 8, 9] as $d) {
                    $dfs($d);
                }
            } else {
                foreach ($digits as $d) {
                    $dfs($cur * 10 + $d);
                }
            }
        };
        $dfs(0);
        return $ans;
    }
}
