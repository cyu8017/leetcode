<?php
// LeetCode 3958 - Minimum Cost To Split Into Ones II
// https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

class Solution {
    function minCost($n) {
        return intdiv($n * ($n - 1), 2);
    }
}
