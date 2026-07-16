// LeetCode 0164 - Maximum Gap
// https://leetcode.com/problems/maximum-gap/

class Solution {
    function maximumGap(array $nums): int {
        if (count($nums) < 2) return 0;
        $low = min($nums);
        $high = max($nums);
        if ($low === $high) return 0;
        $bucketSize = max(1, intdiv($high - $low, count($nums) - 1));
        $bucketCount = intdiv($high - $low, $bucketSize) + 1;
        $mins = array_fill(0, $bucketCount, PHP_INT_MAX);
        $maxs = array_fill(0, $bucketCount, PHP_INT_MIN);
        $used = array_fill(0, $bucketCount, false);
        foreach ($nums as $number) {
            $index = intdiv($number - $low, $bucketSize);
            $used[$index] = true;
            $mins[$index] = min($mins[$index], $number);
            $maxs[$index] = max($maxs[$index], $number);
        }
        $best = 0;
        $previousMax = $low;
        for ($i = 0; $i < $bucketCount; $i++) {
            if (!$used[$i]) continue;
            $best = max($best, $mins[$i] - $previousMax);
            $previousMax = $maxs[$i];
        }
        return $best;
    }
}