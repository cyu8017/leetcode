<?php
// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

class Solution {
    /**
     * @param Integer[][] $rooms
     * @return Boolean
     */
    function canVisitAllRooms($rooms) {
        $seen = [0 => true];
        $stack = [0];
        while (count($stack)) {
            $room = array_pop($stack);
            foreach ($rooms[$room] as $key) {
                if (!isset($seen[$key])) {
                    $seen[$key] = true;
                    $stack[] = $key;
                }
            }
        }
        return count($seen) === count($rooms);
    }
}
