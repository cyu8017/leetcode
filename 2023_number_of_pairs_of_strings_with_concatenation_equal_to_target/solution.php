<?php
// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

class Solution {
    /**
     * @param String[] $nums
     * @param String $target
     * @return Integer
     */
    function numOfPairs($nums, $target) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($i !== $j && $nums[$i] . $nums[$j] === $target) $ans++;
        return $ans;
    }
}
