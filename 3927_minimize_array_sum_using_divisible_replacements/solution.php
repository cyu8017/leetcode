<?php
// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

class Solution {
    function minArraySum($nums) {
        $maximum = 0;
        $present = array_fill(0, 100001, false);
        foreach ($nums as $value) {
            $present[$value] = true;
            if ($value > $maximum) $maximum = $value;
        }
        $best = array_fill(0, $maximum + 1, 0);
        for ($divisor = 1; $divisor <= $maximum; $divisor++) {
            if (!$present[$divisor]) continue;
            for ($multiple = $divisor; $multiple <= $maximum; $multiple += $divisor) {
                if ($best[$multiple] == 0) $best[$multiple] = $divisor;
            }
        }
        $answer = 0;
        foreach ($nums as $value) $answer += $best[$value];
        return $answer;
    }
}
