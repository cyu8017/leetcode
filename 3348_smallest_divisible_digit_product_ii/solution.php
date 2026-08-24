<?php
// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

class Solution {
    function dfs(&$res, $i, $tight, $sameLen, $num, $t) {
        if ($i === count($res)) {
            $prod = 1;
            foreach ($res as $c) {
                $prod *= (ord($c) - 48);
                if ($prod === 0) break;
            }
            return $prod % $t === 0 && $prod > 0;
        }
        $start = ($i === 0) ? '1' : '0';
        if ($tight && $sameLen && $i < strlen($num)) $start = $num[$i];
        for ($cc = ord($start); $cc <= 57; $cc++) {
            $c = chr($cc);
            $res[$i] = $c;
            $nt = $tight && $sameLen && $i < strlen($num) && $c === $num[$i];
            if ($this->dfs($res, $i + 1, $nt, $sameLen, $num, $t)) return true;
        }
        return false;
    }

    function smallestNumber($num, $t) {
        $tt = $t;
        for ($d = 9; $d >= 2; $d--) {
            while ($tt % $d === 0) $tt = intdiv($tt, $d);
        }
        if ($tt > 1) return '-1';
        for ($extra = 0; $extra <= 60; $extra++) {
            $L = strlen($num) + $extra;
            $res = array_fill(0, $L, '0');
            if ($this->dfs($res, 0, true, $extra === 0, $num, $t)) return implode('', $res);
        }
        return '-1';
    }
}
