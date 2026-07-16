<?php
// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

class Solution {
    /**
     * @param int $n
     * @return int
     */
    function magicalString($n) {
        return $this->magical_string($n);
    }

    /**
     * @param int $n
     * @return int
     */
    function magical_string($n) {
        if ($n === 0) {
            return 0;
        }
        $seq = [1, 2, 2];
        $i = 2;
        while (count($seq) < $n) {
            if ($seq[$i] === 1) {
                $seq[] = end($seq) === 2 ? 1 : 2;
            } else {
                $nextVal = end($seq) === 2 ? 1 : 2;
                array_push($seq, $nextVal, $nextVal);
            }
            $i++;
        }
        $slice = array_slice($seq, 0, $n);
        return count(array_filter($slice, fn($value) => $value === 1));
    }
}
