<?php
// LeetCode 0363 - Max Sum of Rectangle No Larger Than K
// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function maxSumSubmatrix($matrix, $k) {
        return $this->max_sum_submatrix($matrix, $k);
    }

    /**
     * @param Integer[][] $matrix
     * @param Integer $k
     * @return Integer
     */
    function max_sum_submatrix($matrix, $k) {
        $rows = count($matrix);
        $cols = $rows === 0 ? 0 : count($matrix[0]);
        $result = PHP_INT_MIN;

        for ($top = 0; $top < $rows; $top++) {
            $colSums = array_fill(0, $cols, 0);
            for ($bottom = $top; $bottom < $rows; $bottom++) {
                $prefixSums = [0];
                $running = 0;
                for ($col = 0; $col < $cols; $col++) {
                    $colSums[$col] += $matrix[$bottom][$col];
                    $running += $colSums[$col];
                    $index = $this->bisectLeft($prefixSums, $running - $k);
                    if ($index < count($prefixSums)) {
                        $result = max($result, $running - $prefixSums[$index]);
                    }
                    $this->insortLeft($prefixSums, $running);
                }
            }
        }

        return $result;
    }

    /**
     * @param Integer[] $array
     * @param Integer $target
     * @return Integer
     */
    private function bisectLeft($array, $target) {
        $left = 0;
        $right = count($array);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($array[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }

    /**
     * @param Integer[] $array
     * @param Integer $value
     * @return void
     */
    private function insortLeft(&$array, $value) {
        $index = $this->bisectLeft($array, $value);
        array_splice($array, $index, 0, [$value]);
    }
}
