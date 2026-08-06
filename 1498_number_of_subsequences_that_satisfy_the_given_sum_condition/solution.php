<?php
class Solution {
    function numSubseq($nums, $target) {
        sort($nums);
        $mod = 1000000007;
        $left = 0;
        $right = count($nums) - 1;
        $ans = 0;
        $powers = array_fill(0, count($nums) + 1, 1);
        for ($i = 1; $i < count($powers); $i++) $powers[$i] = $powers[$i - 1] * 2 % $mod;
        while ($left <= $right) {
            if ($nums[$left] + $nums[$right] <= $target) {
                $ans = ($ans + $powers[$right - $left]) % $mod;
                $left++;
            } else {
                $right--;
            }
        }
        return $ans;
    }
}
