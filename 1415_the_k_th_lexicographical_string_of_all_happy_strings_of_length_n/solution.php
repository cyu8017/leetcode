<?php
class Solution {
    function getHappyString($n, $k) {
        $answer = [];
        $build = function($path) use (&$build, &$answer, $n) {
            if (strlen($path) === $n) {
                $answer[] = $path;
                return;
            }
            foreach (["a", "b", "c"] as $char) {
                if ($path === "" || $path[strlen($path) - 1] !== $char) $build($path . $char);
            }
        };
        $build("");
        return $k <= count($answer) ? $answer[$k - 1] : "";
    }
}
