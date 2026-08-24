<?php
// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function removeInvalidParentheses($s) {
        $isValid = function ($text) {
            $balance = 0;
            $length = strlen($text);
            for ($index = 0; $index < $length; $index++) {
                $char = $text[$index];
                if ($char === "(") {
                    $balance++;
                } elseif ($char === ")") {
                    if ($balance === 0) {
                        return false;
                    }
                    $balance--;
                }
            }
            return $balance === 0;
        };

        $result = [];
        $queue = [$s];
        $visited = [$s => true];
        $found = false;
        while (!empty($queue)) {
            $levelSize = count($queue);
            for ($level = 0; $level < $levelSize; $level++) {
                $current = array_shift($queue);
                if ($isValid($current)) {
                    $result[$current] = true;
                    $found = true;
                }
                if ($found) {
                    continue;
                }
                $length = strlen($current);
                for ($index = 0; $index < $length; $index++) {
                    $char = $current[$index];
                    if ($char !== "(" && $char !== ")") {
                        continue;
                    }
                    $next = substr($current, 0, $index) . substr($current, $index + 1);
                    if (isset($visited[$next])) {
                        continue;
                    }
                    $visited[$next] = true;
                    $queue[] = $next;
                }
            }
        }
        return array_keys($result);
    }
}
