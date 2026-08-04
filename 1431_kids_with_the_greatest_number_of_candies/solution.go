// LeetCode 1431 - Kids With the Greatest Number of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

func kidsWithCandies(candies []int, extraCandies int) []bool {
	maximum := candies[0]
	for _, v := range candies {
		if v > maximum {
			maximum = v
		}
	}
	answer := make([]bool, len(candies))
	for i, v := range candies {
		answer[i] = v+extraCandies >= maximum
	}
	return answer
}
