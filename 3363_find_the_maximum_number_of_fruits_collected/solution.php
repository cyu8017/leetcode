<?php
// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

class Solution {
    function maxCollectedFruits($fruits) {
        $n = count($fruits);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans += $fruits[$i][$i];
            $fruits[$i][$i] = 0;
        }
        $neg = -(1 << 30);
        $dp2 = [];
        $dp3 = [];
        for ($i = 0; $i < $n; $i++) {
            $dp2[$i] = array_fill(0, $n, $neg);
            $dp3[$i] = array_fill(0, $n, $neg);
        }
        $dp2[0][$n - 1] = $fruits[0][$n - 1];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($dp2[$i][$j] === $neg) continue;
                foreach ([-1, 0, 1] as $dj) {
                    $ni = $i + 1;
                    $nj = $j + $dj;
                    if ($ni < $n && $nj >= 0 && $nj < $n && $nj > $ni) {
                        $v = $dp2[$i][$j] + $fruits[$ni][$nj];
                        if ($v > $dp2[$ni][$nj]) $dp2[$ni][$nj] = $v;
                    }
                }
            }
        }
        $dp3[$n - 1][0] = $fruits[$n - 1][0];
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $n; $i++) {
                if ($dp3[$i][$j] === $neg) continue;
                foreach ([-1, 0, 1] as $di) {
                    $ni = $i + $di;
                    $nj = $j + 1;
                    if ($ni >= 0 && $ni < $n && $nj < $n && $ni > $nj) {
                        $v = $dp3[$i][$j] + $fruits[$ni][$nj];
                        if ($v > $dp3[$ni][$nj]) $dp3[$ni][$nj] = $v;
                    }
                }
            }
        }
        $ans += $dp2[$n - 1][$n - 1] + $dp3[$n - 1][$n - 1];
        return $ans;
    }
}
