<?php
// LeetCode 3857 - Minimum Cost to Split Into Ones
// https://leetcode.com/problems/minimum-cost-to-split-into-ones/

class Solution {
    function minCost($n) {
        return $n * ($n - 1) / 2;
    }
}
