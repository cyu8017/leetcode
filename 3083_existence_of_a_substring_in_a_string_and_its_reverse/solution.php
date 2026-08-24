<?php
// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution {
    function isSubstringPresent($s) {
        $st = [];
        for ($i = 0; $i < 26; $i++) $st[] = array_fill(0, 26, false);
        $n = strlen($s);
        for ($i = 0; $i + 1 < $n; $i++)
            $st[ord($s[$i + 1]) - 97][ord($s[$i]) - 97] = true;
        for ($i = 0; $i + 1 < $n; $i++)
            if ($st[ord($s[$i]) - 97][ord($s[$i + 1]) - 97]) return true;
        return false;
    }
}
