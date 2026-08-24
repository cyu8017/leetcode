<?php
// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function numFactoredBinaryTrees($arr) {
        $MOD = 1000000007;
        sort($arr);
        $index = [];
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) $index[$arr[$i]] = $i;
        $dp = array_fill(0, $n, 1);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ($arr[$i] % $arr[$j] === 0) {
                    $right = intdiv($arr[$i], $arr[$j]);
                    if (isset($index[$right])) {
                        $dp[$i] = ($dp[$i] + $dp[$j] * $dp[$index[$right]]) % $MOD;
                    }
                }
            }
            $ans = ($ans + $dp[$i]) % $MOD;
        }
        return $ans;
    }
}
