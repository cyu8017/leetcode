<?php
// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function largestEvenSum($nums, $k) {
        $arr = $nums;
        rsort($arr);
        $sum = 0;
        for ($i = 0; $i < $k; $i++) $sum += $arr[$i];
        if ($sum % 2 === 0) return $sum;
        $ans = -1;
        $oddIn = -1;
        $evenIn = -1;
        $oddOut = -1;
        $evenOut = -1;
        for ($i = $k - 1; $i >= 0; $i--) {
            if ($arr[$i] % 2 !== 0 && $oddIn === -1) $oddIn = $i;
            if ($arr[$i] % 2 === 0 && $evenIn === -1) $evenIn = $i;
        }
        for ($i = $k; $i < count($arr); $i++) {
            if ($arr[$i] % 2 !== 0 && $oddOut === -1) $oddOut = $i;
            if ($arr[$i] % 2 === 0 && $evenOut === -1) $evenOut = $i;
        }
        if ($oddIn !== -1 && $evenOut !== -1) $ans = max($ans, $sum - $arr[$oddIn] + $arr[$evenOut]);
        if ($evenIn !== -1 && $oddOut !== -1) $ans = max($ans, $sum - $arr[$evenIn] + $arr[$oddOut]);
        return $ans;
    }
}
