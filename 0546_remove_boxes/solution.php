<?php
// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

class Solution {
    /**
     * @param Integer[] $boxes
     * @return Integer
     */
    function removeBoxes($boxes) {
        $memo = [];
        $dp = function ($left, $right, $streak) use (&$dp, $boxes, &$memo) {
            if ($left > $right) {
                return 0;
            }
            $state = "{$left},{$right},{$streak}";
            if (array_key_exists($state, $memo)) {
                return $memo[$state];
            }

            while ($right > $left && $boxes[$right] === $boxes[$right - 1]) {
                $right--;
                $streak++;
            }

            $best = ($streak + 1) * ($streak + 1) + $dp($left, $right - 1, 0);
            for ($i = $left; $i < $right; $i++) {
                if ($boxes[$i] === $boxes[$right]) {
                    $candidate = $dp($left, $i, $streak + 1) + $dp($i + 1, $right - 1, 0);
                    $best = max($best, $candidate);
                }
            }

            $memo[$state] = $best;
            return $best;
        };

        return $dp(0, count($boxes) - 1, 0);
    }
}
