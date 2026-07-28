// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

type MountainArray struct {
	arr []int
}

func (this *MountainArray) get(index int) int {
	return this.arr[index]
}

func (this *MountainArray) length() int {
	return len(this.arr)
}

func findInMountainArray(target int, mountainArr *MountainArray) int {
	n := mountainArr.length()
	lo, hi := 0, n-1
	for lo < hi {
		mid := lo + (hi-lo)/2
		if mountainArr.get(mid) < mountainArr.get(mid+1) {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	peak := lo
	lo, hi = 0, peak
	for lo <= hi {
		mid := lo + (hi-lo)/2
		val := mountainArr.get(mid)
		if val == target {
			return mid
		}
		if val < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	lo, hi = peak+1, n-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		val := mountainArr.get(mid)
		if val == target {
			return mid
		}
		if val > target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return -1
}
