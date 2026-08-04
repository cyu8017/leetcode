// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

func distributeCandies(candies int, num_people int) []int {
	ans := make([]int, num_people)
	give := 1
	i := 0
	for candies > 0 {
		take := give
		if take > candies {
			take = candies
		}
		ans[i] += take
		candies -= take
		give++
		i = (i + 1) % num_people
	}
	return ans
}
