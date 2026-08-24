<?php
// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

class Solution {
    function countSeniors($details) {
        $ans = 0;
        foreach ($details as $d) {
            $age = (ord($d[11]) - 48) * 10 + (ord($d[12]) - 48);
            if ($age > 60) $ans++;
        }
        return $ans;
    }
}
