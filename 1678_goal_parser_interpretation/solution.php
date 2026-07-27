<?php
// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

class Solution {
    function interpret($command) {
        return str_replace(["()", "(al)"], ["o", "al"], $command);
    }
}
