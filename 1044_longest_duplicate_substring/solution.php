<?php
// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function longestDupSubstring($s) {
        $mod = 1000000007;
        $base = 911382323;
        $n = strlen($s);
        $nums = [];
        for ($i = 0; $i < $n; $i++) {
            $nums[] = ord($s[$i]);
        }

        $search = function ($length) use ($s, $n, $nums, $mod, $base) {
            if ($length === 0) {
                return 0;
            }
            $h = 0;
            for ($i = 0; $i < $length; $i++) {
                $h = ($h * $base + $nums[$i]) % $mod;
            }
            $seen = [$h => [0]];
            $power = 1;
            for ($i = 0; $i < $length; $i++) {
                $power = ($power * $base) % $mod;
            }
            for ($i = 1; $i <= $n - $length; $i++) {
                $h = ($h * $base - $nums[$i - 1] * $power % $mod + $mod) % $mod;
                $h = ($h + $nums[$i + $length - 1]) % $mod;
                $cur = substr($s, $i, $length);
                if (isset($seen[$h])) {
                    foreach ($seen[$h] as $j) {
                        if (substr($s, $j, $length) === $cur) {
                            return $i;
                        }
                    }
                    $seen[$h][] = $i;
                } else {
                    $seen[$h] = [$i];
                }
            }
            return -1;
        };

        $lo = 0;
        $hi = $n - 1;
        $start = -1;
        $bestLen = 0;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $pos = $search($mid);
            if ($pos >= 0) {
                $start = $pos;
                $bestLen = $mid;
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $start >= 0 ? substr($s, $start, $bestLen) : '';
    }
}
