// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

class Solution {
    function containsNearbyAlmostDuplicate($nums, $indexDiff, $valueDiff) {
        if ($indexDiff <= 0 || $valueDiff < 0) {
            return false;
        }
        $width = $valueDiff + 1;
        $buckets = [];
        foreach ($nums as $i => $num) {
            $bucket = $this->bucketId($num, $width);
            if (isset($buckets[$bucket])) {
                return true;
            }
            if (isset($buckets[$bucket - 1]) && abs($num - $buckets[$bucket - 1]) <= $valueDiff) {
                return true;
            }
            if (isset($buckets[$bucket + 1]) && abs($num - $buckets[$bucket + 1]) <= $valueDiff) {
                return true;
            }
            if (count($buckets) >= $indexDiff) {
                $old = $nums[$i - $indexDiff];
                unset($buckets[$this->bucketId($old, $width)]);
            }
            $buckets[$bucket] = $num;
        }
        return false;
    }

    private function bucketId($num, $width) {
        return $num >= 0 ? intdiv($num, $width) : intdiv($num + 1, $width) - 1;
    }
}
