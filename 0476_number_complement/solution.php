<?php
// LeetCode 0476 - Number Complement
// https://leetcode.com/problems/number-complement/

class Solution {
    /**
     * @param int $num
     * @return int
     */
    function findComplement($num) {
        return $this->find_complement($num);
    }

    /**
     * @param int $num
     * @return int
     */
    function find_complement($num) {
        $mask = $num;
        $mask |= $mask >> 1;
        $mask |= $mask >> 2;
        $mask |= $mask >> 4;
        $mask |= $mask >> 8;
        $mask |= $mask >> 16;
        return $num ^ $mask;
    }
}
