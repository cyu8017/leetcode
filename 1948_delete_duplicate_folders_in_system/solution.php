<?php

class Solution {
    /**
     * @param String[][] $paths
     * @return String[][]
     */
    function deleteDuplicateFolder($paths) {
        $root = [];
        foreach ($paths as $path) {
            $node = &$root;
            foreach ($path as $folder) {
                if (!isset($node[$folder])) {
                    $node[$folder] = [];
                }
                $node = &$node[$folder];
            }
            unset($node);
        }

        $dup = [];
        $serialOf = [];

        $serialize = function (&$node, $nodeId) use (&$serialize, &$dup, &$serialOf) {
            if (empty($node)) {
                return '';
            }
            $parts = [];
            $names = array_keys($node);
            sort($names);
            foreach ($names as $name) {
                $childId = $nodeId . '/' . $name;
                $parts[] = $name . '(' . $serialize($node[$name], $childId) . ')';
            }
            $serial = implode('', $parts);
            if ($serial !== '') {
                if (isset($dup[$serial])) {
                    $dup[$serial] = true;
                } else {
                    $dup[$serial] = false;
                }
                $serialOf[$nodeId] = $serial;
            }
            return $serial;
        };

        $serialize($root, '');

        $ans = [];
        $collect = function (&$node, $path, $nodeId) use (&$collect, &$ans, &$dup, &$serialOf) {
            foreach ($node as $name => &$child) {
                $childId = $nodeId . '/' . $name;
                $serial = $serialOf[$childId] ?? '';
                if ($serial !== '' && !empty($dup[$serial])) {
                    continue;
                }
                $path[] = $name;
                $ans[] = $path;
                $collect($child, $path, $childId);
                array_pop($path);
            }
        };

        $collect($root, [], '');
        return $ans;
    }
}
