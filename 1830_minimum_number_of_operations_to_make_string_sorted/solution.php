<?php
// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function makeStringSorted($s) {
        $mod = 1000000007;
        $n = strlen($s);

        $fact = array_fill(0, $n + 1, 1);
        for ($i = 2; $i <= $n; $i++) {
            $fact[$i] = ($fact[$i - 1] * $i) % $mod;
        }

        $invFact = array_fill(0, $n + 1, 1);
        $invFact[$n] = $this->modPow($fact[$n], $mod - 2, $mod);
        for ($i = $n - 1; $i >= 0; $i--) {
            $invFact[$i] = ($invFact[$i + 1] * ($i + 1)) % $mod;
        }

        $freq = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $freq[ord($s[$i]) - ord('a')]++;
        }

        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - ord('a');
            for ($smaller = 0; $smaller < $c; $smaller++) {
                if ($freq[$smaller] === 0) {
                    continue;
                }
                $freq[$smaller]--;
                $ways = $fact[$n - $i - 1];
                foreach ($freq as $count) {
                    $ways = ($ways * $invFact[$count]) % $mod;
                }
                $ans = ($ans + $ways) % $mod;
                $freq[$smaller]++;
            }
            $freq[$c]--;
        }

        return $ans;
    }

    /**
     * @param int $base
     * @param int $exp
     * @param int $mod
     * @return int
     */
    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
