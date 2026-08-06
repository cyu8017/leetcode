<?php
class Solution {
    function watchedVideosByFriends($watchedVideos, $friends, $id, $level) {
        $queue = [[$id, 0]];
        $seen = [$id => true];
        $people = [];
        while ($queue) {
            [$person, $distance] = array_shift($queue);
            if ($distance === $level) {
                $people[] = $person;
                continue;
            }
            foreach ($friends[$person] as $friend) {
                if (!isset($seen[$friend])) {
                    $seen[$friend] = true;
                    $queue[] = [$friend, $distance + 1];
                }
            }
        }
        $counts = [];
        foreach ($people as $person) {
            foreach ($watchedVideos[$person] as $video) {
                $counts[$video] = ($counts[$video] ?? 0) + 1;
            }
        }
        $keys = array_keys($counts);
        usort($keys, function($a, $b) use ($counts) {
            if ($counts[$a] !== $counts[$b]) return $counts[$a] <=> $counts[$b];
            return $a <=> $b;
        });
        return $keys;
    }
}
