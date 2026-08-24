<?php
// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

class Solution {
    private function gcd($a, $b) {
        while ($b) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    private function lcm($a, $b) {
        return intdiv($a, $this->gcd($a, $b)) * $b;
    }

    function minimumIncrements($nums, $target) {
        $m = count($target);
        $N = 1 << $m;
        $inf = 1e18;
        $dp = array_fill(0, $N, $inf);
        $dp[0] = 0;
        foreach ($nums as $x) {
            $ndp = $dp;
            for ($mask = 0; $mask < $N; $mask++) {
                for ($sub = 1; $sub < $N; $sub++) {
                    $L = 1;
                    $ok = true;
                    for ($i = 0; $i < $m; $i++) {
                        if ($sub & (1 << $i)) {
                            $L = $this->lcm($L, $target[$i]);
                            if ($L > 1000000000) { $ok = false; break; }
                        }
                    }
                    if (!$ok) continue;
                    $cost = ($L - $x % $L) % $L;
                    $nmask = $mask | $sub;
                    if ($dp[$mask] + $cost < $ndp[$nmask]) $ndp[$nmask] = $dp[$mask] + $cost;
                }
            }
            $dp = $ndp;
        }
        return $dp[$N - 1];
    }
}
