<?php
// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maximumSum($arr) {
        $keep = $delete = $ans = $arr[0];
        $n = count($arr);
        for ($i = 1; $i < $n; $i++) {
            $x = $arr[$i];
            $delete = max($keep, $delete + $x);
            $keep = max($keep + $x, $x);
            $ans = max($ans, $keep, $delete);
        }
        return $ans;
    }
}
