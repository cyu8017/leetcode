<?php
// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Float[] $succProb
     * @param Integer $start_node
     * @param Integer $end_node
     * @return Float
     */
    function maxProbability($n, $edges, $succProb, $start_node, $end_node) {
        $graph = array_fill(0, $n, []);
        $m = count($edges);
        for ($i = 0; $i < $m; $i++) {
            $a = $edges[$i][0];
            $b = $edges[$i][1];
            $p = $succProb[$i];
            $graph[$a][] = [$b, $p];
            $graph[$b][] = [$a, $p];
        }
        $heap = new SplPriorityQueue();
        $heap->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $heap->insert($start_node, 1.0);
        $best = array_fill(0, $n, 0.0);
        $best[$start_node] = 1.0;
        while (!$heap->isEmpty()) {
            $item = $heap->extract();
            $node = $item['data'];
            $probability = $item['priority'];
            if ($node === $end_node) {
                return $probability;
            }
            if ($probability < $best[$node]) {
                continue;
            }
            foreach ($graph[$node] as [$neighbor, $edgeProbability]) {
                $candidate = $probability * $edgeProbability;
                if ($candidate > $best[$neighbor]) {
                    $best[$neighbor] = $candidate;
                    $heap->insert($neighbor, $candidate);
                }
            }
        }
        return 0.0;
    }
}
