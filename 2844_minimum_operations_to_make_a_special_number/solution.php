<?php
// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution {
    function minimumOperations($num) {
        $n = strlen($num);
        $ans = $n;
        if (strpos($num, '0') !== false) $ans = min($ans, $n - 1);
        foreach (['00', '25', '50', '75'] as $t) {
            $j = $n - 1;
            while ($j >= 0 && $num[$j] !== $t[1]) $j--;
            if ($j < 0) continue;
            $i = $j - 1;
            while ($i >= 0 && $num[$i] !== $t[0]) $i--;
            if ($i < 0) continue;
            $ans = min($ans, $n - $i - 2);
        }
        return $ans;
    }
}
