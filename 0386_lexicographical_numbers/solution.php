<?php
// LeetCode 0386 - Lexicographical Numbers
// https://leetcode.com/problems/lexicographical-numbers/

class Solution {
    /**
     * @param Integer $n
     * @return Integer[]
     */
    function lexicalOrder($n) {
        return $this->lexical_order($n);
    }

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function lexical_order($n) {
        $result = [];
        $dfs = function ($current) use (&$dfs, &$result, $n) {
            if ($current > $n) {
                return;
            }
            $result[] = $current;
            $dfs($current * 10);
            if ($current % 10 < 9) {
                $dfs($current + 1);
            }
        };

        $dfs(1);
        return $result;
    }
}
