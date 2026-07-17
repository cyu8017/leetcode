<?php
// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

class Solution {
    const MOD = 1000000007;

    /**
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function waysToFillArray($queries) {
        $ans = [];
        foreach ($queries as $query) {
            $n = $query[0];
            $value = $query[1];
            $ways = 1;
            $d = 2;
            while ($d * $d <= $value) {
                if ($value % $d === 0) {
                    $exp = 0;
                    while ($value % $d === 0) {
                        $value = intdiv($value, $d);
                        $exp++;
                    }
                    $ways = $ways * $this->combMod($n + $exp - 1, $exp) % self::MOD;
                }
                $d += $d === 2 ? 1 : 2;
            }
            if ($value > 1) {
                $ways = $ways * ($n % self::MOD) % self::MOD;
            }
            $ans[] = $ways;
        }
        return $ans;
    }

    private function combMod($a, $b) {
        $num = 1;
        $den = 1;
        for ($i = 1; $i <= $b; $i++) {
            $num = $num * (($a - $b + $i) % self::MOD) % self::MOD;
            $den = $den * ($i % self::MOD) % self::MOD;
        }
        return $num * $this->powMod($den, self::MOD - 2) % self::MOD;
    }

    private function powMod($base, $exp) {
        $result = 1;
        $base %= self::MOD;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = $result * $base % self::MOD;
            }
            $base = $base * $base % self::MOD;
            $exp >>= 1;
        }
        return $result;
    }
}
