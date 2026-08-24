<?php
// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

class Solution {
    /**
     * @param int[] $nums
     * @return bool
     */
    function circularArrayLoop($nums) {
        return $this->circular_array_loop($nums);
    }

    /**
     * @param int[] $nums
     * @return bool
     */
    function circular_array_loop($nums) {
        $values = $nums;
        $length = count($values);

        $nextIndex = function (int $index) use (&$values, $length): int {
            $next = $index + $values[$index];
            return (($next % $length) + $length) % $length;
        };

        for ($start = 0; $start < $length; $start++) {
            if ($values[$start] === 0) {
                continue;
            }

            $forward = $values[$start] > 0;
            $slow = $start;
            $fast = $start;

            while (true) {
                $slow = $nextIndex($slow);
                $fast = $nextIndex($nextIndex($fast));
                if (
                    $values[$slow] * ($forward ? 1 : -1) <= 0 ||
                    $values[$fast] * ($forward ? 1 : -1) <= 0 ||
                    $values[$nextIndex($fast)] * ($forward ? 1 : -1) <= 0
                ) {
                    break;
                }
                if ($slow === $fast) {
                    if ($slow === $nextIndex($slow)) {
                        break;
                    }
                    return true;
                }
            }

            $index = $start;
            $direction = $values[$start];
            while ($values[$index] * $direction > 0) {
                $values[$index] = 0;
                $index = $nextIndex($index);
            }
        }

        return false;
    }
}
