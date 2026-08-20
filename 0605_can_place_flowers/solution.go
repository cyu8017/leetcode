// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

func canPlaceFlowers(flowerbed []int, n int) bool {
	if n == 0 {
		return true
	}
	bed := append([]int(nil), flowerbed...)
	for i := 0; i < len(bed); i++ {
		if bed[i] == 1 {
			continue
		}
		leftEmpty := i == 0 || bed[i-1] == 0
		rightEmpty := i == len(bed)-1 || bed[i+1] == 0
		if leftEmpty && rightEmpty {
			bed[i] = 1
			n--
			if n == 0 {
				return true
			}
		}
	}
	return false
}
