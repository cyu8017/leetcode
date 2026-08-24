<?php
// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function kSimilarity($s1, $s2) {
        if ($s1 === $s2) return 0;
        $neighbors = function($s) use ($s2) {
            $arr = str_split($s);
            $i = 0;
            while ($arr[$i] === $s2[$i]) $i++;
            $res = [];
            $len = count($arr);
            for ($j = $i + 1; $j < $len; $j++) {
                if ($arr[$j] === $s2[$i] && $arr[$j] !== $s2[$j]) {
                    $tmp = $arr[$i];
                    $arr[$i] = $arr[$j];
                    $arr[$j] = $tmp;
                    $res[] = implode('', $arr);
                    $tmp = $arr[$i];
                    $arr[$i] = $arr[$j];
                    $arr[$j] = $tmp;
                }
            }
            return $res;
        };
        $queue = [$s1];
        $dist = [$s1 => 0];
        $qi = 0;
        while ($qi < count($queue)) {
            $cur = $queue[$qi++];
            $d = $dist[$cur];
            foreach ($neighbors($cur) as $nxt) {
                if ($nxt === $s2) return $d + 1;
                if (!isset($dist[$nxt])) {
                    $dist[$nxt] = $d + 1;
                    $queue[] = $nxt;
                }
            }
        }
        return -1;
    }
}
