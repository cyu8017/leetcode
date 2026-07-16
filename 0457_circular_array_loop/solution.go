// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

func circularArrayLoop(nums []int) bool {
	length := len(nums)

	nextIndex := func(index int) int {
		step := nums[index]
		return ((index+step)%length + length) % length
	}

	for start := 0; start < length; start++ {
		if nums[start] == 0 {
			continue
		}

		direction := 1
		if nums[start] < 0 {
			direction = -1
		}
		slow, fast := start, start

		for {
			slow = nextIndex(slow)
			fast = nextIndex(nextIndex(fast))

			if nums[slow]*direction <= 0 || nums[fast]*direction <= 0 ||
				nums[nextIndex(fast)]*direction <= 0 {
				break
			}
			if slow == fast {
				if slow == nextIndex(slow) {
					break
				}
				return true
			}
		}

		index := start
		value := nums[start]
		for nums[index]*value > 0 {
			nums[index] = 0
			index = nextIndex(index)
		}
	}

	return false
}
