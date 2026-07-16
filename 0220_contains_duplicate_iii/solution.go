// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

func containsNearbyAlmostDuplicate(nums []int, indexDiff int, valueDiff int) bool {
	if indexDiff <= 0 || valueDiff < 0 {
		return false
	}
	width := int64(valueDiff) + 1
	buckets := make(map[int64]int64)

	bucketId := func(num int64) int64 {
		if num >= 0 {
			return num / width
		}
		return (num+1)/width - 1
	}

	for i, num := range nums {
		value := int64(num)
		bucket := bucketId(value)
		if _, ok := buckets[bucket]; ok {
			return true
		}
		if prev, ok := buckets[bucket-1]; ok && abs(value-prev) <= int64(valueDiff) {
			return true
		}
		if next, ok := buckets[bucket+1]; ok && abs(value-next) <= int64(valueDiff) {
			return true
		}
		if len(buckets) >= indexDiff {
			delete(buckets, bucketId(int64(nums[i-indexDiff])))
		}
		buckets[bucket] = value
	}
	return false
}

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}
