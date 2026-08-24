<?php
// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution {
    function findKOr($nums, $k) {
        $ans = 0;
        for ($b = 0; $b < 31; $b++) {
            $cnt = 0;
            foreach ($nums as $v) if (($v & (1 << $b)) !== 0) $cnt++;
            if ($cnt >= $k) $ans |= 1 << $b;
        }
        return $ans;
    }
}
