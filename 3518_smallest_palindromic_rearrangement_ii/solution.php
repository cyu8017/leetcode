<?php
// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

class Solution {
    private $MAX = 1000001;

    private function nCk($n, $kk) {
        if ($kk < 0 || $kk > $n) return 0;
        $res = 1;
        if ($kk > $n - $kk) $kk = $n - $kk;
        for ($i = 1; $i <= $kk; $i++) {
            $res = intdiv($res * ($n - $i + 1), $i);
            if ($res >= $this->MAX) return $this->MAX;
        }
        return $res;
    }

    private function countArr($h) {
        $total = 0;
        foreach ($h as $f) $total += $f;
        $res = 1;
        foreach ($h as $f) {
            $res *= $this->nCk($total, $f);
            if ($res >= $this->MAX) return $this->MAX;
            $total -= $f;
        }
        return $res;
    }

    function smallestPalindrome($s, $k) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $odd = 0;
        foreach ($cnt as $c) if ($c % 2 !== 0) $odd++;
        if ($odd > 1) return '';
        $half = array_fill(0, 26, 0);
        $mid = '';
        for ($i = 0; $i < 26; $i++) {
            $half[$i] = intdiv($cnt[$i], 2);
            if ($cnt[$i] % 2 !== 0) $mid = chr(97 + $i);
        }
        if ($this->countArr($half) < $k) return '';
        $halfLen = 0;
        foreach ($half as $f) $halfLen += $f;
        $left = '';
        for ($t = 0; $t < $halfLen; $t++) {
            for ($i = 0; $i < 26; $i++) {
                if ($half[$i] === 0) continue;
                $half[$i]--;
                $arr = $this->countArr($half);
                if ($arr >= $k) {
                    $left .= chr(97 + $i);
                    break;
                }
                $k -= $arr;
                $half[$i]++;
            }
        }
        $res = $left;
        if ($mid !== '') $res .= $mid;
        for ($i = strlen($left) - 1; $i >= 0; $i--) $res .= $left[$i];
        return $res;
    }
}
