<?php
// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

class Solution {
    private $MOD = 1000000007;

    function countKSubsequencesWithMaxBeauty($s, $k) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $vals = [];
        foreach ($freq as $f) if ($f > 0) $vals[] = $f;
        rsort($vals);
        if (count($vals) < $k) return 0;
        $threshold = $vals[$k - 1];
        $need = 0;
        $avail = 0;
        $prod = 1;
        foreach ($vals as $v) {
            if ($v > $threshold) {
                $prod = ($prod * $v) % $this->MOD;
                $need++;
            } else if ($v === $threshold) $avail++;
        }
        $remain = $k - $need;
        $prod = ($prod * $this->comb($avail, $remain)) % $this->MOD;
        for ($i = 0; $i < $remain; $i++) $prod = ($prod * $threshold) % $this->MOD;
        return (int)$prod;
    }

    private function modPow($a, $b) {
        $res = 1;
        $a %= $this->MOD;
        while ($b > 0) {
            if ($b % 2 === 1) $res = ($res * $a) % $this->MOD;
            $a = ($a * $a) % $this->MOD;
            $b = intdiv($b, 2);
        }
        return $res;
    }

    private function comb($n, $r) {
        if ($r < 0 || $r > $n) return 0;
        $num = 1;
        $den = 1;
        for ($i = 0; $i < $r; $i++) {
            $num = ($num * ($n - $i)) % $this->MOD;
            $den = ($den * ($i + 1)) % $this->MOD;
        }
        return ($num * $this->modPow($den, $this->MOD - 2)) % $this->MOD;
    }
}
