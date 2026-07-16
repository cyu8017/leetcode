// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

func majorityElement(nums []int) []int {
	var candidate1 *int
	var candidate2 *int
	count1 := 0
	count2 := 0

	for _, num := range nums {
		switch {
		case candidate1 != nil && num == *candidate1:
			count1++
		case candidate2 != nil && num == *candidate2:
			count2++
		case count1 == 0:
			value := num
			candidate1 = &value
			count1 = 1
		case count2 == 0:
			value := num
			candidate2 = &value
			count2 = 1
		default:
			count1--
			count2--
		}
	}

	count1 = 0
	count2 = 0
	for _, num := range nums {
		if candidate1 != nil && num == *candidate1 {
			count1++
		} else if candidate2 != nil && num == *candidate2 {
			count2++
		}
	}

	threshold := len(nums) / 3
	result := []int{}
	if count1 > threshold {
		result = append(result, *candidate1)
	}
	if candidate2 != nil && (candidate1 == nil || *candidate2 != *candidate1) && count2 > threshold {
		result = append(result, *candidate2)
	}
	return result
}
