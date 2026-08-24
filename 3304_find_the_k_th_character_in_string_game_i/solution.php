<?php
// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution {
    function kthCharacter($k) {
        $s = 'a';
        while (strlen($s) < $k) {
            $n = strlen($s);
            $add = '';
            for ($i = 0; $i < $n; $i++) {
                $add .= chr(97 + ((ord($s[$i]) - 97 + 1) % 26));
            }
            $s .= $add;
        }
        return $s[$k - 1];
    }
}
