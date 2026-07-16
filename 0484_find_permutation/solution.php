<?php
// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

class Solution {
    /**
     * @param string $s
     * @return int[]
     */
    function findPermutation($s) {
        return $this->find_permutation($s);
    }

    /**
     * @param string $s
     * @return int[]
     */
    function find_permutation($s) {
        $stack = [1];
        $result = [];
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            if ($s[$index] === 'I') {
                while (count($stack) > 0) {
                    $result[] = array_pop($stack);
                }
            }
            $stack[] = count($stack) + count($result) + 1;
        }
        while (count($stack) > 0) {
            $result[] = array_pop($stack);
        }
        return $result;
    }
}
