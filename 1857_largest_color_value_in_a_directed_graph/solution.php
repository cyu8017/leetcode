<?php
// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution {
    /**
     * @param String $colors
     * @param Integer[][] $edges
     * @return Integer
     */
    function largestPathValue($colors, $edges) {
        $n = strlen($colors);
        $indegree = array_fill(0, $n, 0);
        $adjacency = array_fill(0, $n, []);

        foreach ($edges as [$fromNode, $toNode]) {
            $adjacency[$fromNode][] = $toNode;
            $indegree[$toNode]++;
        }

        $queue = new SplQueue();
        for ($node = 0; $node < $n; $node++) {
            if ($indegree[$node] === 0) {
                $queue->enqueue($node);
            }
        }

        $dp = array_fill(0, $n, array_fill(0, 26, 0));
        for ($node = 0; $node < $n; $node++) {
            $dp[$node][ord($colors[$node]) - ord('a')] = 1;
        }

        $processed = 0;
        $answer = 0;

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            $processed++;
            $answer = max($answer, max($dp[$node]));

            foreach ($adjacency[$node] as $neighbor) {
                $neighborColor = ord($colors[$neighbor]) - ord('a');
                for ($colorIndex = 0; $colorIndex < 26; $colorIndex++) {
                    $candidate = $dp[$node][$colorIndex];
                    if ($colorIndex === $neighborColor) {
                        $candidate++;
                    }
                    if ($candidate > $dp[$neighbor][$colorIndex]) {
                        $dp[$neighbor][$colorIndex] = $candidate;
                    }
                }

                $indegree[$neighbor]--;
                if ($indegree[$neighbor] === 0) {
                    $queue->enqueue($neighbor);
                }
            }
        }

        return $processed === $n ? $answer : -1;
    }
}
