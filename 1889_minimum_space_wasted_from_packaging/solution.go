// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

import "sort"

func minWastedSpace(packages []int, boxes [][]int) int {
	sortedPackages := append([]int(nil), packages...)
	sort.Ints(sortedPackages)

	prefix := make([]int, len(sortedPackages))
	running := 0
	for i, value := range sortedPackages {
		running += value
		prefix[i] = running
	}

	const mod = 1_000_000_007
	answer := 1 << 62

	for _, supplier := range boxes {
		sortedSupplier := append([]int(nil), supplier...)
		sort.Ints(sortedSupplier)

		start := 0
		wasted := 0
		for _, box := range sortedSupplier {
			end := bisectRightFrom(sortedPackages, box, start)
			if end == start {
				continue
			}
			packageSum := prefix[end-1]
			if start > 0 {
				packageSum -= prefix[start-1]
			}
			wasted += box*(end-start) - packageSum
			start = end
		}
		if start == len(sortedPackages) && wasted < answer {
			answer = wasted
		}
	}

	if answer == 1<<62 {
		return -1
	}
	return answer % mod
}

func bisectRightFrom(values []int, target int, lo int) int {
	hi := len(values)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if values[mid] <= target {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}
