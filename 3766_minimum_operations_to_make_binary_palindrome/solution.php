<?php
// LeetCode 3766 - Minimum Operations to Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

class Solution {
    function minOperations($nums) {
        $PALS = [];
        $N = 1 << 14;
        $isPalindrome = function($s) {
            $m = strlen($s);
            for ($i = 0; $i < intdiv($m, 2); $i++) if ($s[$i] !== $s[$m - 1 - $i]) return false;
            return true;
        };
        for ($i = 0; $i < $N; $i++) {
            $sb = '';
            $x = $i;
            if ($x === 0) $sb = '0';
            else {
                while ($x > 0) {
                    $sb .= chr(48 + ($x & 1));
                    $x >>= 1;
                }
                $sb = strrev($sb);
            }
            if ($isPalindrome($sb)) $PALS[] = $i;
        }
        $lowerBound = function($x) use ($PALS) {
            $lo = 0;
            $hi = count($PALS);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($PALS[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            return $lo;
        };
        $ans = array_fill(0, count($nums), 0);
        for ($k = 0; $k < count($nums); $k++) {
            $x = $nums[$k];
            $it = $lowerBound($x);
            $t = 9007199254740991;
            if ($it < count($PALS)) $t = $PALS[$it] - $x;
            if ($it > 0) $t = min($t, $x - $PALS[$it - 1]);
            $ans[$k] = $t;
        }
        return $ans;
    }
}
