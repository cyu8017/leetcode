<?php
// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

class Solution {
    function perfectPairs($nums) {
        $n = count($nums);
        $absNums = [];
        foreach ($nums as $x) $absNums[] = abs($x);
        sort($absNums);
        $ans = 0;
        $j = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($j < $i + 1) $j = $i + 1;
            while ($j < $n && $absNums[$j] <= 2 * $absNums[$i]) $j++;
            $ans += $j - $i - 1;
        }
        return $ans;
    }
}
