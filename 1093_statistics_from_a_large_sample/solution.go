// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

func sampleStats(count []int) []float64 {
	total := 0
	for _, c := range count {
		total += c
	}
	minimum := 0
	for i, c := range count {
		if c > 0 {
			minimum = i
			break
		}
	}
	maximum := 0
	for i := 255; i >= 0; i-- {
		if count[i] > 0 {
			maximum = i
			break
		}
	}
	sum := 0
	for i, c := range count {
		sum += i * c
	}
	mean := float64(sum) / float64(total)
	mode := 0
	for i := 1; i < 256; i++ {
		if count[i] > count[mode] {
			mode = i
		}
	}
	mid1 := (total + 1) / 2
	mid2 := (total + 2) / 2
	seen := 0
	first, second := -1, -1
	for i, c := range count {
		seen += c
		if first < 0 && seen >= mid1 {
			first = i
		}
		if second < 0 && seen >= mid2 {
			second = i
			break
		}
	}
	median := float64(first+second) / 2
	return []float64{float64(minimum), float64(maximum), mean, median, float64(mode)}
}
