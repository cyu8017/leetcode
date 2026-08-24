<?php
// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

class Solution {
    /**
     * @param String $s
     * @param String[] $words
     * @return Integer
     */
    function expressiveWords($s, $words) {
        $groups = function($text) {
            $result = [];
            $i = 0;
            $n = strlen($text);
            while ($i < $n) {
                $j = $i;
                while ($j < $n && $text[$j] === $text[$i]) $j++;
                $result[] = [ord($text[$i]), $j - $i];
                $i = $j;
            }
            return $result;
        };
        $target = $groups($s);
        $ans = 0;
        foreach ($words as $word) {
            $source = $groups($word);
            if (count($source) !== count($target)) continue;
            $ok = true;
            $len = count($source);
            for ($i = 0; $i < $len; $i++) {
                if ($source[$i][0] !== $target[$i][0]) { $ok = false; break; }
                $c1 = $source[$i][1];
                $c2 = $target[$i][1];
                if ($c1 > $c2 || ($c1 !== $c2 && $c2 < 3)) { $ok = false; break; }
            }
            if ($ok) $ans++;
        }
        return $ans;
    }
}
