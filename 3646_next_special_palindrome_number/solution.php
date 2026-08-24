<?php
// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

class Solution {
    function specialPalindrome($n) {
        $cands = [];
        $halfCnt = [];
        $mid = 0;
        $halfLen = 0;
        $dfs = function($pos, $cur) use (&$dfs, &$cands, &$halfCnt, &$mid, &$halfLen) {
            if ($pos === $halfLen) {
                $left = implode('', $cur);
                $s = $left;
                if ($mid > 0) $s .= $mid;
                for ($i = strlen($left) - 1; $i >= 0; $i--) $s .= $left[$i];
                $cands[] = (int)$s;
                return;
            }
            for ($d = 1; $d <= 9; $d++) {
                if ($halfCnt[$d] === 0) continue;
                $halfCnt[$d]--;
                $cur[] = $d;
                $dfs($pos + 1, $cur);
                array_pop($cur);
                $halfCnt[$d]++;
            }
        };
        $gen = function($mask) use (&$cands, &$halfCnt, &$mid, &$halfLen, $dfs) {
            $total = 0;
            $odd = 0;
            for ($d = 1; $d <= 9; $d++) {
                if ((($mask >> $d) & 1) !== 0) {
                    $total += $d;
                    if ($d % 2 === 1) $odd++;
                }
            }
            if ($total === 0 || $total > 18 || $odd > 1) return;
            $halfCnt = array_fill(0, 10, 0);
            $mid = 0;
            for ($d = 1; $d <= 9; $d++) {
                if ((($mask >> $d) & 1) === 0) continue;
                $halfCnt[$d] = intdiv($d, 2);
                if ($d % 2 === 1) $mid = $d;
            }
            $halfLen = intdiv($total, 2);
            $dfs(0, []);
        };
        for ($mask = 1; $mask < (1 << 10); $mask++) {
            if (($mask & 1) !== 0) continue;
            $gen($mask);
        }
        sort($cands);
        foreach ($cands as $v)
            if ($v > $n) return $v;
        return -1;
    }
}
