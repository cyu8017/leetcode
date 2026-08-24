<?php
// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution {
    function valueAfterKSeconds($n, $k) {
        $mod = 1000000007;
        $a = array_fill(0, $n, 1);
        while ($k-- > 0) {
            for ($i = 1; $i < $n; $i++) $a[$i] = ($a[$i] + $a[$i - 1]) % $mod;
        }
        return $a[$n - 1];
    }
}
