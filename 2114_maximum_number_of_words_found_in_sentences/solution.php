<?php
// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution {
    /**
     * @param String[] $sentences
     * @return Integer
     */
    function mostWordsFound($sentences) {
        $ans = 0;
        foreach ($sentences as $s) {
            $c = 1;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) if ($s[$i] === ' ') $c++;
            $ans = max($ans, $c);
        }
        return $ans;
    }
}
