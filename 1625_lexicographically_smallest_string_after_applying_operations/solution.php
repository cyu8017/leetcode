<?php
// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution {
    /**
     * @param String $s
     * @param Integer $a
     * @param Integer $b
     * @return String
     */
    function findLexSmallestString($s, $a, $b) {
        $seen = [$s => true];
        $q = [$s];
        $ans = $s;
        for ($qi = 0; $qi < count($q); $qi++) {
            $cur = $q[$qi];
            if ($cur < $ans) {
                $ans = $cur;
            }
            $chars = str_split($cur);
            $n = count($chars);
            for ($i = 0; $i < $n; $i++) {
                if ($i % 2 === 1) {
                    $chars[$i] = (string)((intval($chars[$i]) + $a) % 10);
                }
            }
            $add = implode("", $chars);
            $rot = substr($cur, -$b) . substr($cur, 0, $n - $b);
            foreach ([$add, $rot] as $nxt) {
                if (!isset($seen[$nxt])) {
                    $seen[$nxt] = true;
                    $q[] = $nxt;
                }
            }
        }
        return $ans;
    }
}
