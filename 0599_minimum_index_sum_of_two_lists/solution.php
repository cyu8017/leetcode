<?php
// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution {
    function findRestaurant($list1, $list2) {
        $index1 = [];
        for ($i = 0; $i < count($list1); ++$i) $index1[$list1[$i]] = $i;
        $best = PHP_INT_MAX;
        $answer = [];
        for ($j = 0; $j < count($list2); ++$j) {
            if (!isset($index1[$list2[$j]])) continue;
            $total = $index1[$list2[$j]] + $j;
            if ($total < $best) {
                $best = $total;
                $answer = [$list2[$j]];
            } elseif ($total === $best) {
                $answer[] = $list2[$j];
            }
        }
        return $answer;
    }
}
