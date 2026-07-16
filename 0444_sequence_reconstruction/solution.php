// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

class Solution {
    /**
     * @param int[] $nums
     * @param int[][] $sequences
     * @return bool
     */
    function sequenceReconstruction($nums, $sequences) {
        return $this->sequence_reconstruction($nums, $sequences);
    }

    /**
     * @param int[] $nums
     * @param int[][] $sequences
     * @return bool
     */
    function sequence_reconstruction($nums, $sequences) {
        $indegree = [];
        $graph = [];
        $seenEdges = [];
        foreach ($nums as $value) {
            $indegree[$value] = 0;
            $graph[$value] = [];
        }

        foreach ($sequences as $sequence) {
            for ($index = 0; $index < count($sequence) - 1; $index++) {
                $left = $sequence[$index];
                $right = $sequence[$index + 1];
                $edgeKey = $left . "," . $right;
                if (isset($seenEdges[$edgeKey])) {
                    continue;
                }
                $seenEdges[$edgeKey] = true;
                $graph[$left][] = $right;
                $indegree[$right]++;
            }
        }

        $queue = array_values(array_filter($nums, fn($value) => $indegree[$value] === 0));
        $order = [];
        while (count($queue) > 0) {
            if (count($queue) > 1) {
                return false;
            }
            $node = array_shift($queue);
            $order[] = $node;
            foreach ($graph[$node] as $neighbor) {
                $indegree[$neighbor]--;
                if ($indegree[$neighbor] === 0) {
                    $queue[] = $neighbor;
                }
            }
        }

        return $order === $nums;
    }
}
