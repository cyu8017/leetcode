<?php
// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

class Solution {
    function evenProduct($nums) {
        $n = count($nums);
        $total = intdiv($n * ($n + 1), 2);
        $oddLen = 0;
        $odd = 0;
        foreach ($nums as $x) {
            if ($x % 2 === 1) {
                $odd++;
                $oddLen += $odd;
            } else $odd = 0;
        }
        return $total - $oddLen;
    }
}
