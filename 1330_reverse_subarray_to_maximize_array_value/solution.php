<?php
class Solution {
    function maxValueAfterReverse($nums) {
        $base = 0;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) $base += abs($nums[$i] - $nums[$i + 1]);
        $gain = 0;
        $low = 1000000000;
        $high = -1000000000;
        for ($i = 0; $i < $n - 1; $i++) {
            $a = $nums[$i];
            $b = $nums[$i + 1];
            $gain = max($gain, abs($nums[0] - $b) - abs($a - $b), abs($nums[$n - 1] - $a) - abs($a - $b));
            $low = min($low, max($a, $b));
            $high = max($high, min($a, $b));
        }
        return $base + max($gain, 2 * ($high - $low));
    }
}
