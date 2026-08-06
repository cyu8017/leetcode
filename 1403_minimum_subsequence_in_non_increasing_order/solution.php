<?php
class Solution {
    function minSubsequence($nums) {
        rsort($nums);
        $answer = [];
        $chosen = 0;
        $total = array_sum($nums);
        foreach ($nums as $value) {
            $answer[] = $value;
            $chosen += $value;
            if ($chosen > $total - $chosen) return $answer;
        }
        return $answer;
    }
}
