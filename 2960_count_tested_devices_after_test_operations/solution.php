<?php
// LeetCode 2960 - Count Tested Devices After Test Operations
// https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution {
    function countTestedDevices($batteryPercentages) {
        $ans = 0;
        foreach ($batteryPercentages as $b) {
            if ($b > $ans) $ans++;
        }
        return $ans;
    }
}
