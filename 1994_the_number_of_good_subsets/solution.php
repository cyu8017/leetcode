<?php
// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfGoodSubsets($nums) {
        $MOD = 1000000007;
        $primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        $masks = array_fill(0, 31, 0);
        for ($x = 2; $x < 31; $x++) {
            $m = 0;
            $y = $x;
            $ok = true;
            foreach ($primes as $i => $p) {
                if ($y % $p === 0) {
                    if (intdiv($y, $p) % $p === 0) {
                        $ok = false;
                        break;
                    }
                    $m |= 1 << $i;
                    $y = intdiv($y, $p);
                }
            }
            $masks[$x] = $ok ? $m : -1;
        }

        $cnt = array_fill(0, 31, 0);
        foreach ($nums as $v) {
            $cnt[$v]++;
        }

        $pCount = count($primes);
        $dp = array_fill(0, 1 << $pCount, 0);
        $dp[0] = 1;
        for ($x = 2; $x < 31; $x++) {
            if ($cnt[$x] === 0 || $masks[$x] < 0) {
                continue;
            }
            $m = $masks[$x];
            for ($state = (1 << $pCount) - 1; $state >= 0; $state--) {
                if ($state & $m) {
                    continue;
                }
                $dp[$state | $m] = ($dp[$state | $m] + $dp[$state] * $cnt[$x]) % $MOD;
            }
        }

        $ans = 0;
        for ($i = 1; $i < count($dp); $i++) {
            $ans = ($ans + $dp[$i]) % $MOD;
        }
        $ones = 1;
        for ($i = 0; $i < $cnt[1]; $i++) {
            $ones = ($ones * 2) % $MOD;
        }
        return ($ans * $ones) % $MOD;
    }
}
