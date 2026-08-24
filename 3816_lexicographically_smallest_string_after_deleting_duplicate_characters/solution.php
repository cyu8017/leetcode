<?php
// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

class Solution {
    function lexSmallestAfterDeletion($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $stk = [];
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            while (count($stk) > 0 && $stk[count($stk) - 1] > $c
                    && $cnt[ord($stk[count($stk) - 1]) - 97] > 1) {
                $cnt[ord($stk[count($stk) - 1]) - 97]--;
                array_pop($stk);
            }
            $stk[] = $c;
        }
        while ($cnt[ord($stk[count($stk) - 1]) - 97] > 1) {
            $cnt[ord($stk[count($stk) - 1]) - 97]--;
            array_pop($stk);
        }
        return implode('', $stk);
    }
}
