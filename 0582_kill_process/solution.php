<?php
// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

class Solution {
    function killProcess($pid, $ppid, $kill) {
        $children = [];
        for ($i = 0; $i < count($pid); ++$i) {
            if (!isset($children[$ppid[$i]])) $children[$ppid[$i]] = [];
            $children[$ppid[$i]][] = $pid[$i];
        }
        $result = [];
        $queue = [$kill];
        while ($queue) {
            $process = array_shift($queue);
            $result[] = $process;
            $kids = $children[$process] ?? null;
            if ($kids) foreach ($kids as $child) $queue[] = $child;
        }
        return $result;
    }
}
