<?php
// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

class FileSystem {
    private $paths = ['' => -1];

    function __construct() {}

    /**
     * @param String $path
     * @param Integer $value
     * @return Boolean
     */
    function createPath($path, $value) {
        if (isset($this->paths[$path])) return false;
        $parent = substr($path, 0, strrpos($path, '/'));
        if (!isset($this->paths[$parent])) return false;
        $this->paths[$path] = $value;
        return true;
    }

    /**
     * @param String $path
     * @return Integer
     */
    function get($path) {
        return $this->paths[$path] ?? -1;
    }
}
