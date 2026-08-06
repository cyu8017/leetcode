<?php
class Solution {
    function longestSubarray($nums) {
        $left = 0;
        $zeros = 0;
        $ans = 0;
        foreach ($nums as $right => $x) {
            if ($x === 0) $zeros++;
            while ($zeros > 1) {
                if ($nums[$left] === 0) $zeros--;
                $left++;
            }
            $ans = max($ans, $right - $left);
        }
        return $ans;
    }
}
