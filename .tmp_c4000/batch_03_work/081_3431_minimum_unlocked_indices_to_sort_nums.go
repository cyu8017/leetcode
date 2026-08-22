// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

func minUnlockedIndices(nums []int, locked []int) int {
	n := len(nums)
	target := append([]int(nil), nums...)
	// sort target
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if target[j] < target[i] {
				target[i], target[j] = target[j], target[i]
			}
		}
	}
	// Check if possible: locked positions must already match
	for i := 0; i < n; i++ {
		if locked[i] == 1 && nums[i] != target[i] {
			// may still swap through unlocked - actually locked cannot change
			// so if locked and wrong value, impossible unless value equals somehow
		}
	}
	// Simpler approach for values in {1,2,3}:
	ans := 0
	// find positions where order wrong
	maxSeen := 0
	for i := 0; i < n; i++ {
		if nums[i] < maxSeen {
			// need unlock something
		}
		if nums[i] > maxSeen {
			maxSeen = nums[i]
		}
	}
	// For 1,2,3 specifically:
	pos3, pos1 := -1, -1
	for i := 0; i < n; i++ {
		if nums[i] == 3 {
			pos3 = i
		}
	}
	for i := n - 1; i >= 0; i-- {
		if nums[i] == 1 {
			pos1 = i
			break
		}
	}
	if pos1 == -1 || pos3 == -1 || pos3 < pos1 {
		// check already sorted
		ok := true
		for i := 1; i < n; i++ {
			if nums[i] < nums[i-1] {
				ok = false
				break
			}
		}
		if ok {
			return 0
		}
	}
	// unlock all between first misplaced
	need := false
	for i := 1; i < n; i++ {
		if nums[i] < nums[i-1] {
			need = true
			break
		}
	}
	if !need {
		return 0
	}
	// count locked in range where 3 appears before 1
	left, right := n, -1
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if nums[i] > nums[j] {
				if i < left {
					left = i
				}
				if j > right {
					right = j
				}
			}
		}
	}
	if right < left {
		return 0
	}
	for i := left; i <= right; i++ {
		if locked[i] == 1 {
			ans++
		}
	}
	// verify unlockable: if we unlock those, can we sort? For 1..3 bubbles
	tmp := append([]int(nil), nums...)
	lock := append([]int(nil), locked...)
	for i := left; i <= right; i++ {
		lock[i] = 0
	}
	changed := true
	for changed {
		changed = false
		for i := 0; i+1 < n; i++ {
			if lock[i] == 0 && lock[i+1] == 0 && tmp[i] > tmp[i+1] {
				tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
				changed = true
			}
		}
	}
	for i := 1; i < n; i++ {
		if tmp[i] < tmp[i-1] {
			return -1
		}
	}
	return ans
}
