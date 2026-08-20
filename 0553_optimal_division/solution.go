// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

import (
	"fmt"
	"strconv"
	"strings"
)

func optimalDivision(nums []int) string {
	if len(nums) == 1 {
		return strconv.Itoa(nums[0])
	}
	if len(nums) == 2 {
		return fmt.Sprintf("%d/%d", nums[0], nums[1])
	}
	parts := make([]string, len(nums)-1)
	for i, num := range nums[1:] {
		parts[i] = strconv.Itoa(num)
	}
	return fmt.Sprintf("%d/(%s)", nums[0], strings.Join(parts, "/"))
}
