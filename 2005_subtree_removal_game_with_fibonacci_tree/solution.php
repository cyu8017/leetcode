<?php
// LeetCode 2005 - Subtree Removal Game with Fibonacci Tree
// https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function findGameWinner($n) {
        return $n % 6 !== 1;
    }
}
