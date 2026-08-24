<?php
// LeetCode 0158 - Read N Characters Given read4 II - Call Multiple Times
// https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

class Solution {
    function read(string $file, array $queries): array {
        $fileIndex = 0;
        $buffer = [];
        $results = [];
        foreach ($queries as $query) {
            $copied = 0;
            while ($copied < $query) {
                if (count($buffer) === 0) {
                    $buffer = str_split(substr($file, $fileIndex, 4));
                    $fileIndex += count($buffer);
                    if (count($buffer) === 0) {
                        break;
                    }
                }
                $amount = min($query - $copied, count($buffer));
                array_splice($buffer, 0, $amount);
                $copied += $amount;
            }
            $results[] = $copied;
        }
        return $results;
    }
}
