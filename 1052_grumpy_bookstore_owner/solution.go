// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	base := 0
	for i, c := range customers {
		if grumpy[i] == 0 {
			base += c
		}
	}
	gain, best := 0, 0
	for i, c := range customers {
		if grumpy[i] == 1 {
			gain += c
		}
		if i >= minutes && grumpy[i-minutes] == 1 {
			gain -= customers[i-minutes]
		}
		if gain > best {
			best = gain
		}
	}
	return base + best
}
