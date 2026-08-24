<?php
// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution {
    function sortArrayByParityII($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $even = 0;
        $odd = 1;
        foreach ($nums as $x) {
            if ($x % 2 === 0) { $ans[$even] = $x; $even += 2; }
            else { $ans[$odd] = $x; $odd += 2; }
        }
        return $ans;
    }
}
