<?php
class Solution {
    function longestSubarray($nums, $limit) {
        $low = [];
        $high = [];
        $left = 0;
        $answer = 0;
        foreach ($nums as $right => $value) {
            while ($low && $nums[$low[count($low) - 1]] > $value) array_pop($low);
            while ($high && $nums[$high[count($high) - 1]] < $value) array_pop($high);
            $low[] = $right;
            $high[] = $right;
            while ($nums[$high[0]] - $nums[$low[0]] > $limit) {
                $left++;
                if ($low[0] < $left) array_shift($low);
                if ($high[0] < $left) array_shift($high);
            }
            $answer = max($answer, $right - $left + 1);
        }
        return $answer;
    }
}
