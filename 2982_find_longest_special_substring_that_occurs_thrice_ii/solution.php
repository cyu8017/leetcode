<?php
// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

class Solution {
    function maximumLength($s) {
        $groups = array_fill(0, 26, []);
        $n = strlen($s);
        for ($i = 0; $i < $n; ) {
            $j = $i;
            while ($j < $n && $s[$j] === $s[$i]) $j++;
            $groups[ord($s[$i]) - 97][] = $j - $i;
            $i = $j;
        }
        $ans = -1;
        for ($c = 0; $c < 26; $c++) {
            $arr = $groups[$c];
            if (count($arr) === 0) continue;
            rsort($arr);
            for ($L = $arr[0]; $L >= 1; $L--) {
                $cnt = 0;
                foreach ($arr as $g) {
                    if ($g >= $L) $cnt += $g - $L + 1;
                }
                if ($cnt >= 3) {
                    if ($L > $ans) $ans = $L;
                    break;
                }
            }
        }
        return $ans;
    }
}
