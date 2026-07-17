<?php
// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

class Solution {
    /**
     * @param String $num
     * @param Integer $k
     * @return Integer
     */
    function getMinSwaps($num, $k) {
        $target = str_split($num);
        for ($i = 0; $i < $k; $i++) {
            $this->nextPermutation($target);
        }

        $source = str_split($num);
        $swaps = 0;
        for ($i = 0; $i < count($source); $i++) {
            if ($source[$i] === $target[$i]) {
                continue;
            }
            $j = $i;
            while ($source[$j] !== $target[$i]) {
                $j++;
            }
            while ($j > $i) {
                [$source[$j], $source[$j - 1]] = [$source[$j - 1], $source[$j]];
                $swaps++;
                $j--;
            }
        }
        return $swaps;
    }

    /**
     * @param string[] $arr
     */
    private function nextPermutation(&$arr) {
        $i = count($arr) - 2;
        while ($i >= 0 && $arr[$i] >= $arr[$i + 1]) {
            $i--;
        }
        if ($i < 0) {
            $arr = array_reverse($arr);
            return;
        }
        $j = count($arr) - 1;
        while ($arr[$j] <= $arr[$i]) {
            $j--;
        }
        [$arr[$i], $arr[$j]] = [$arr[$j], $arr[$i]];
        $left = $i + 1;
        $right = count($arr) - 1;
        while ($left < $right) {
            [$arr[$left], $arr[$right]] = [$arr[$right], $arr[$left]];
            $left++;
            $right--;
        }
    }
}
