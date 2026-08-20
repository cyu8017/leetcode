// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

func hasGroupsSizeX(deck []int) bool {
	count := map[int]int{}
	for _, x := range deck {
		count[x]++
	}
	g := 0
	for _, c := range count {
		g = gcd(g, c)
	}
	return g >= 2
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
