<?php
// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

class Solution {
    private function isPrime($n) {
        if ($n < 2) return false;
        for ($i = 2; $i <= intdiv($n, $i); $i++) {
            if ($n % $i === 0) return false;
        }
        return true;
    }

    function mostFrequentPrime($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $cnt = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                for ($a = -1; $a <= 1; $a++) {
                    for ($b = -1; $b <= 1; $b++) {
                        if ($a === 0 && $b === 0) continue;
                        $x = $i + $a;
                        $y = $j + $b;
                        $v = $mat[$i][$j];
                        while ($x >= 0 && $x < $m && $y >= 0 && $y < $n) {
                            $v = $v * 10 + $mat[$x][$y];
                            if ($this->isPrime($v)) $cnt[$v] = ($cnt[$v] ?? 0) + 1;
                            $x += $a;
                            $y += $b;
                        }
                    }
                }
            }
        }
        $ans = -1;
        $mx = 0;
        foreach ($cnt as $key => $value) {
            if ($mx < $value || ($mx === $value && $ans < $key)) {
                $mx = $value;
                $ans = $key;
            }
        }
        return $ans;
    }
}
