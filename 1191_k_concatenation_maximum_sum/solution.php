<?php
// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function kConcatenationMaxSum($arr, $k) {
        $mod = 1000000007;
        $kadane = function ($nums) {
            $best = $cur = 0;
            foreach ($nums as $x) {
                $cur = max(0, $cur + $x);
                $best = max($best, $cur);
            }
            return $best;
        };
        $one = $kadane($arr);
        if ($k === 1) return $one % $mod;
        $two = $kadane(array_merge($arr, $arr));
        $total = array_sum($arr);
        if ($total > 0) return max($one, $two + $total * ($k - 2)) % $mod;
        return max($one, $two) % $mod;
    }
}
