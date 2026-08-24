<?php
// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

class Solution {
    function phonePrefix($numbers) {
        sort($numbers);
        for ($i = 0; $i + 1 < count($numbers); $i++) {
            if (strlen($numbers[$i]) <= strlen($numbers[$i + 1]) && strncmp($numbers[$i + 1], $numbers[$i], strlen($numbers[$i])) === 0)
                return false;
        }
        return true;
    }
}
