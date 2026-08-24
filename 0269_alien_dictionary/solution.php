<?php
// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

class Solution {
    /**
     * @param String[] $words
     * @return String
     */
    function alienOrder($words) {
        $graph = [];
        $indegree = [];

        foreach ($words as $word) {
            $length = strlen($word);
            for ($i = 0; $i < $length; $i++) {
                $char = $word[$i];
                if (!isset($graph[$char])) {
                    $graph[$char] = [];
                    $indegree[$char] = 0;
                }
            }
        }

        for ($i = 0; $i < count($words) - 1; $i++) {
            $first = $words[$i];
            $second = $words[$i + 1];
            if (strlen($first) > strlen($second) && strncmp($first, $second, strlen($second)) === 0) {
                return '';
            }
            $limit = min(strlen($first), strlen($second));
            for ($j = 0; $j < $limit; $j++) {
                $left = $first[$j];
                $right = $second[$j];
                if ($left !== $right) {
                    if (!in_array($right, $graph[$left], true)) {
                        $graph[$left][] = $right;
                        $indegree[$right]++;
                    }
                    break;
                }
            }
        }

        $queue = [];
        foreach ($indegree as $char => $degree) {
            if ($degree === 0) {
                $queue[] = $char;
            }
        }

        $order = '';
        while (!empty($queue)) {
            $char = array_shift($queue);
            $order .= $char;
            foreach ($graph[$char] as $next) {
                $indegree[$next]--;
                if ($indegree[$next] === 0) {
                    $queue[] = $next;
                }
            }
        }

        return strlen($order) === count($indegree) ? $order : '';
    }
}
