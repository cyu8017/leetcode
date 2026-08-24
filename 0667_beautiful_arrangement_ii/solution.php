<?php
// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution {
    function constructArray($n, $k) {
        $res = array_fill(0, $n, 0);
        $idx = 0;
        for ($i = 1; $i <= $n - $k; ++$i) $res[$idx++] = $i;
        $left = $n - $k + 1;
        $right = $n;
        $takeHigh = true;
        while ($left <= $right) {
            if ($takeHigh) $res[$idx++] = $right--;
            else $res[$idx++] = $left++;
            $takeHigh = !$takeHigh;
        }
        return $res;
    }
}
