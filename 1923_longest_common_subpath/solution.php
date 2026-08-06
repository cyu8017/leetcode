<?php
// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $paths
     * @return Integer
     */
    function longestCommonSubpath($n, $paths) {
        $lo = 0;
        $hi = PHP_INT_MAX;
        foreach ($paths as $path) {
            $hi = min($hi, count($path));
        }
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->hasCommon($paths, $mid)) {
                $lo = $mid;
            } else {
                $hi = $mid - 1;
            }
        }
        return $lo;
    }

    private function hasCommon($paths, $length) {
        if ($length === 0) {
            return true;
        }
        $base1 = 911382323;
        $mod1 = 1000000007;
        $base2 = 972663749;
        $mod2 = 1000000009;
        $pow1 = $this->modPow($base1, $length, $mod1);
        $pow2 = $this->modPow($base2, $length, $mod2);
        $common = null;

        foreach ($paths as $path) {
            $len = count($path);
            if ($len < $length) {
                return false;
            }
            $h1 = 0;
            $h2 = 0;
            $seen = [];
            for ($i = 0; $i < $len; $i++) {
                $h1 = ($h1 * $base1 + $path[$i] + 1) % $mod1;
                $h2 = ($h2 * $base2 + $path[$i] + 1) % $mod2;
                if ($i >= $length) {
                    $h1 = ($h1 - ($path[$i - $length] + 1) * $pow1) % $mod1;
                    if ($h1 < 0) {
                        $h1 += $mod1;
                    }
                    $h2 = ($h2 - ($path[$i - $length] + 1) * $pow2) % $mod2;
                    if ($h2 < 0) {
                        $h2 += $mod2;
                    }
                }
                if ($i >= $length - 1) {
                    $seen["$h1,$h2"] = true;
                }
            }
            if ($common === null) {
                $common = $seen;
            } else {
                $common = array_intersect_key($common, $seen);
            }
            if (!$common) {
                return false;
            }
        }
        return true;
    }

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
