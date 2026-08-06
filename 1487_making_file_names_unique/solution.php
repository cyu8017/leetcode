<?php
class Solution {
    function getFolderNames($names) {
        $used = [];
        $ans = [];
        foreach ($names as $name) {
            if (!isset($used[$name])) {
                $candidate = $name;
            } else {
                $k = $used[$name];
                while (isset($used["$name($k)"])) $k++;
                $candidate = "$name($k)";
                $used[$name] = $k + 1;
            }
            $used[$candidate] = 1;
            $ans[] = $candidate;
        }
        return $ans;
    }
}
