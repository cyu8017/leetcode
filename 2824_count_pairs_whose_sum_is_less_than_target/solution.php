<?php
// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution {
    function countPairs($nums, $target) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                if ($nums[$i] + $nums[$j] < $target) $ans++;
        return $ans;
    }
}
