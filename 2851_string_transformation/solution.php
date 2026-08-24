<?php
// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

class Solution {
    private $MOD = 1000000007;

    function numberOfWays($s, $t, $k) {
        $n = strlen($s);
        $ss = $s . $s;
        $found = false;
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            if (substr($ss, $i, $n) === $t) {
                $cnt++;
                $found = true;
            }
        }
        if (!$found) return 0;
        $same = $s === $t;
        $pk = $this->modPow($n - 1, $k);
        $invn = $this->modPow($n, $this->MOD - 2);
        $sign = ($k % 2 === 1) ? ($this->MOD - 1) : 1;
        $waysSame = (($pk + (($n - 1) % $this->MOD) * $sign % $this->MOD) % $this->MOD * $invn) % $this->MOD;
        $waysDiff = (($pk - $sign + $this->MOD) % $this->MOD * $invn) % $this->MOD;
        if ($same) return (int)$waysSame;
        return (int)(($waysDiff * $cnt) % $this->MOD);
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
}
