<?php
// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer[]
     */
    function addNegabinary($arr1, $arr2) {
        $i = count($arr1) - 1;
        $j = count($arr2) - 1;
        $carry = 0;
        $ans = [];
        while ($i >= 0 || $j >= 0 || $carry) {
            $total = $carry;
            if ($i >= 0) {
                $total += $arr1[$i];
                $i--;
            }
            if ($j >= 0) {
                $total += $arr2[$j];
                $j--;
            }
            $ans[] = $total & 1;
            $carry = -($total >> 1);
        }
        while (count($ans) > 1 && end($ans) === 0) {
            array_pop($ans);
        }
        return array_reverse($ans);
    }
}
