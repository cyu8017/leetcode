<?php
// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

class Solution {
    function asteroidCollision($asteroids) {
        $stack = [];
        foreach ($asteroids as $asteroid) {
            $alive = true;
            while ($alive && count($stack) > 0 && $asteroid < 0 && $stack[count($stack) - 1] > 0) {
                if ($stack[count($stack) - 1] < -$asteroid) { array_pop($stack); continue; }
                if ($stack[count($stack) - 1] === -$asteroid) array_pop($stack);
                $alive = false;
            }
            if ($alive) $stack[] = $asteroid;
        }
        return $stack;
    }
}
