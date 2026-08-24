<?php
// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

class Solution {
    /**
     * @param String $s
     * @param Integer[] $indices
     * @param String[] $sources
     * @param String[] $targets
     * @return String
     */
    function findReplaceString($s, $indices, $sources, $targets) {
        $replaceLen = [];
        $replaceStr = [];
        $kn = count($indices);
        for ($k = 0; $k < $kn; $k++) {
            $i = $indices[$k];
            if (substr($s, $i, strlen($sources[$k])) === $sources[$k]) {
                $replaceLen[$i] = strlen($sources[$k]);
                $replaceStr[$i] = $targets[$k];
            }
        }
        $out = "";
        $i = 0;
        $n = strlen($s);
        while ($i < $n) {
            if (isset($replaceStr[$i])) {
                $out .= $replaceStr[$i];
                $i += $replaceLen[$i];
            } else {
                $out .= $s[$i];
                $i++;
            }
        }
        return $out;
    }
}
