<?php
// LeetCode 0171 - Excel Sheet Column Number
// https://leetcode.com/problems/excel-sheet-column-number/

class Solution {
    function titleToNumber(string $columnTitle): int {
        $result = 0;
        for ($i = 0; $i < strlen($columnTitle); $i++) {
            $result = $result * 26 + ord($columnTitle[$i]) - ord("A") + 1;
        }
        return $result;
    }
}
