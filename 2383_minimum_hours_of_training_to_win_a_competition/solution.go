// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

func minNumberOfHours(initialEnergy int, initialExperience int, energy []int, experience []int) int {
	ans := 0
	en, ex := initialEnergy, initialExperience
	for i := range energy {
		if en <= energy[i] {
			need := energy[i] - en + 1
			ans += need
			en += need
		}
		if ex <= experience[i] {
			need := experience[i] - ex + 1
			ans += need
			ex += need
		}
		en -= energy[i]
		ex += experience[i]
	}
	return ans
}
