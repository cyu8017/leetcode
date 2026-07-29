<?php
// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

class Solution {
    /**
     * @param String $source
     * @param String $target
     * @return Integer
     */
    function shortestWay($source, $target) {
        $sourceSet = [];
        $slen = strlen($source);
        for ($i = 0; $i < $slen; $i++) {
            $sourceSet[$source[$i]] = true;
        }
        $n = strlen($target);
        for ($i = 0; $i < $n; $i++) {
            if (!isset($sourceSet[$target[$i]])) {
                return -1;
            }
        }
        $ans = 0;
        $i = 0;
        while ($i < $n) {
            $ans++;
            for ($j = 0; $j < $slen; $j++) {
                if ($i < $n && $target[$i] === $source[$j]) {
                    $i++;
                }
            }
        }
        return $ans;
    }
}
