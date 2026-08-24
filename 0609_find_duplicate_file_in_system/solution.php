<?php
// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution {
    function findDuplicate($paths) {
        $contentToPaths = [];
        foreach ($paths as $entry) {
            $tokens = explode(" ", $entry);
            $directory = $tokens[0];
            for ($i = 1; $i < count($tokens); ++$i) {
                $fileInfo = $tokens[$i];
                $open = strpos($fileInfo, "(");
                $name = substr($fileInfo, 0, $open);
                $content = substr($fileInfo, $open + 1, strlen($fileInfo) - $open - 2);
                if (!isset($contentToPaths[$content])) $contentToPaths[$content] = [];
                $contentToPaths[$content][] = $directory . "/" . $name;
            }
        }
        $result = [];
        foreach ($contentToPaths as $group) {
            if (count($group) > 1) $result[] = $group;
        }
        return $result;
    }
}
