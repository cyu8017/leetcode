<?php
// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortEvenOdd($nums) {
        $even = [];
        $odd = [];
        for ($i = 0; $i < count($nums); $i++) {
            if ($i % 2 === 0) $even[] = $nums[$i];
            else $odd[] = $nums[$i];
        }
        sort($even);
        rsort($odd);
        $ei = 0;
        $oi = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($i % 2 === 0) $nums[$i] = $even[$ei++];
            else $nums[$i] = $odd[$oi++];
        }
        return $nums;
    }
}
