<?php
// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $pivot
     * @return Integer[]
     */
    function pivotArray($nums, $pivot) {
        $ans = array_fill(0, count($nums), 0);
        $i = 0;
        foreach ($nums as $x) if ($x < $pivot) $ans[$i++] = $x;
        foreach ($nums as $x) if ($x === $pivot) $ans[$i++] = $x;
        foreach ($nums as $x) if ($x > $pivot) $ans[$i++] = $x;
        return $ans;
    }
}
