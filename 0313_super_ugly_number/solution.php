<?php
// LeetCode 0313 - Super Ugly Number
// https://leetcode.com/problems/super-ugly-number/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $primes
     * @return Integer
     */
    function nthSuperUglyNumber($n, $primes) {
        $ugly = [1];
        $pointers = array_fill(0, count($primes), 0);
        while (count($ugly) < $n) {
            $nextValues = [];
            foreach ($primes as $index => $prime) {
                $nextValues[] = $ugly[$pointers[$index]] * $prime;
            }
            $nextUgly = min($nextValues);
            $ugly[] = $nextUgly;
            foreach ($primes as $index => $prime) {
                if ($nextUgly === $ugly[$pointers[$index]] * $prime) {
                    $pointers[$index]++;
                }
            }
        }
        return $ugly[count($ugly) - 1];
    }
}
