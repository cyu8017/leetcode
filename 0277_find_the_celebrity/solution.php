// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function findCelebrity($graph) {
        $n = count($graph);
        $candidate = 0;
        for ($person = 1; $person < $n; $person++) {
            if ($graph[$candidate][$person] === 1) {
                $candidate = $person;
            }
        }
        for ($person = 0; $person < $n; $person++) {
            if ($person === $candidate) {
                continue;
            }
            if ($graph[$candidate][$person] === 1 || $graph[$person][$candidate] === 0) {
                return -1;
            }
        }
        return $candidate;
    }
}
