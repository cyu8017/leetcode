<?php
// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

class FileSystem {
    private $root;

    function __construct() {
        $this->root = ["isFile" => false, "content" => "", "children" => []];
    }

    function ls($path) {
        if ($path === "/") {
            $keys = array_keys($this->root["children"]);
            sort($keys);
            return $keys;
        }
        $parts = array_values(array_filter(explode("/", $path), function($p) { return $p !== ""; }));
        $node = &$this->root;
        foreach ($parts as $part) $node = &$node["children"][$part];
        if ($node["isFile"]) return [$parts[count($parts) - 1]];
        $keys = array_keys($node["children"]);
        sort($keys);
        return $keys;
    }

    function mkdir($path) {
        $node = &$this->root;
        foreach (array_values(array_filter(explode("/", $path), function($p) { return $p !== ""; })) as $part) {
            if (!isset($node["children"][$part])) {
                $node["children"][$part] = ["isFile" => false, "content" => "", "children" => []];
            }
            $node = &$node["children"][$part];
        }
    }

    function addContentToFile($filePath, $content) {
        $parts = array_values(array_filter(explode("/", $filePath), function($p) { return $p !== ""; }));
        $node = &$this->root;
        for ($i = 0; $i + 1 < count($parts); ++$i) {
            if (!isset($node["children"][$parts[$i]])) {
                $node["children"][$parts[$i]] = ["isFile" => false, "content" => "", "children" => []];
            }
            $node = &$node["children"][$parts[$i]];
        }
        $name = $parts[count($parts) - 1];
        if (!isset($node["children"][$name])) {
            $node["children"][$name] = ["isFile" => false, "content" => "", "children" => []];
        }
        $node["children"][$name]["isFile"] = true;
        $node["children"][$name]["content"] .= $content;
    }

    function readContentFromFile($filePath) {
        $node = &$this->root;
        foreach (array_values(array_filter(explode("/", $filePath), function($p) { return $p !== ""; })) as $part) {
            $node = &$node["children"][$part];
        }
        return $node["content"];
    }
}
