<?php
// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaximumXOR($nums) {
        return $this->find_maximum_xor($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function find_maximum_xor($nums) {
        $maximum = max($nums);
        $maxBit = $maximum === 0 ? 0 : intval(floor(log($maximum, 2))) + 1;
        $root = [];
        $best = 0;

        foreach ($nums as $number) {
            $node = &$root;
            for ($bit = $maxBit - 1; $bit >= 0; $bit--) {
                $current = ($number >> $bit) & 1;
                if (!isset($node[$current])) {
                    $node[$current] = [];
                }
                $node = &$node[$current];
            }
            unset($node);
        }

        foreach ($nums as $number) {
            $node = $root;
            $candidate = 0;
            for ($bit = $maxBit - 1; $bit >= 0; $bit--) {
                $current = ($number >> $bit) & 1;
                $target = 1 - $current;
                if (isset($node[$target])) {
                    $candidate |= 1 << $bit;
                    $node = $node[$target];
                } else {
                    $node = $node[$current];
                }
            }
            $best = max($best, $candidate);
        }

        return $best;
    }
}
