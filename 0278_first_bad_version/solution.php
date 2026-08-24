<?php
// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

function isBadVersion($version) {
    global $badVersion;
    return $version >= $badVersion;
}

class Solution {
    /**
     * @param Integer $n
     * @param Integer $bad
     * @return Integer
     */
    function firstBadVersion($n, $bad = 1) {
        global $badVersion;
        $badVersion = $bad;
        $left = 1;
        $right = $n;
        while ($left < $right) {
            $mid = $left + intdiv($right - $left, 2);
            if (isBadVersion($mid)) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }
        return $left;
    }
}
