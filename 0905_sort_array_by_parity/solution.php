<?php
// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

class Solution {
    function sortArrayByParity($nums) {
        $i = 0;
        $n = count($nums);
        for ($j = 0; $j < $n; $j++) {
            if ($nums[$j] % 2 === 0) {
                $tmp = $nums[$i];
                $nums[$i] = $nums[$j];
                $nums[$j] = $tmp;
                $i++;
            }
        }
        return $nums;
    }
}
