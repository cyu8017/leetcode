<?php
// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

class Solution {
    const MOD = 1000000007;

    private function modPow($a, $b) {
        $res = 1;
        $a %= self::MOD;
        while ($b > 0) {
            if ($b & 1) $res = (int)(($res * $a) % self::MOD);
            $a = (int)(($a * $a) % self::MOD);
            $b >>= 1;
        }
        return $res;
    }

    function numberOfSequence($n, $sick) {
        $MOD = self::MOD;
        $fact = array_fill(0, $n + 1, 0);
        $invFact = array_fill(0, $n + 1, 0);
        $fact[0] = 1;
        for ($i = 1; $i <= $n; $i++) $fact[$i] = (int)(($fact[$i - 1] * $i) % $MOD);
        $invFact[$n] = $this->modPow($fact[$n], $MOD - 2);
        for ($i = $n; $i > 0; $i--) $invFact[$i - 1] = (int)(($invFact[$i] * $i) % $MOD);
        $m = count($sick);
        $totalEmpty = $n - $m;
        $ans = $fact[$totalEmpty];
        $prev = -1;
        foreach ($sick as $s) {
            $gap = $s - $prev - 1;
            if ($prev === -1) $ans = (int)(($ans * $invFact[$gap]) % $MOD);
            else if ($gap > 0) $ans = (int)((($ans * $invFact[$gap]) % $MOD) * $this->modPow(2, $gap - 1) % $MOD);
            $prev = $s;
        }
        $gap2 = $n - $prev - 1;
        $ans = (int)(($ans * $invFact[$gap2]) % $MOD);
        return $ans;
    }
}
