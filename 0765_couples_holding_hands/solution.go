// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

func minSwapsCouples(row []int) int {
	pos := map[int]int{}
	for i, person := range row {
		pos[person] = i
	}
	swaps := 0
	for i := 0; i < len(row); i += 2 {
		partner := row[i] ^ 1
		if row[i+1] == partner {
			continue
		}
		j := pos[partner]
		pos[row[i+1]] = j
		row[j] = row[i+1]
		row[i+1] = partner
		pos[partner] = i + 1
		swaps++
	}
	return swaps
}
