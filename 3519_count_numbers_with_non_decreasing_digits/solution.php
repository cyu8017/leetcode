<?php
// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

class Solution {
    private $MOD = 1000000007;

    private function toDigits($s, $b) {
        if ($s === '0') return [0];
        $digs = [];
        while (!(strlen($s) === 1 && $s[0] === '0')) {
            $rem = 0;
            $q = '';
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) {
                $cur = $rem * 10 + (ord($s[$i]) - 48);
                $d = intdiv($cur, $b);
                $rem = $cur % $b;
                if (strlen($q) > 0 || $d !== 0) $q .= (string)$d;
            }
            $digs[] = $rem;
            $s = strlen($q) === 0 ? '0' : $q;
        }
        return array_reverse($digs);
    }

    private function dec($s) {
        $a = str_split($s);
        $i = count($a) - 1;
        while ($i >= 0 && $a[$i] === '0') { $a[$i] = '9'; $i--; }
        if ($i < 0) return '0';
        $a[$i] = chr(ord($a[$i]) - 1);
        $t = implode('', $a);
        $p = 0;
        while ($p + 1 < strlen($t) && $t[$p] === '0') $p++;
        return substr($t, $p);
    }

    private function countUpto($digs, $b) {
        $m = count($digs);
        $memo = [];
        $dfs = function($pos, $last, $tight) use (&$dfs, &$memo, $m, $digs, $b) {
            if ($pos === $m) return 1;
            $key = $pos . ',' . $last . ',' . ($tight ? 1 : 0);
            if (isset($memo[$key])) return $memo[$key];
            $up = $tight ? $digs[$pos] : $b - 1;
            $res = 0;
            for ($d = $last; $d <= $up; $d++)
                $res = ($res + $dfs($pos + 1, $d, $tight && $d === $up)) % 1000000007;
            return $memo[$key] = $res;
        };
        return $dfs(0, 0, true);
    }

    function countNumbers($l, $r, $b) {
        $rd = $this->toDigits($r, $b);
        $ld = $this->toDigits($this->dec($l), $b);
        return ($this->countUpto($rd, $b) - $this->countUpto($ld, $b) + $this->MOD) % $this->MOD;
    }
}
