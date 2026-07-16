// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

var ones = []string{
	"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
	"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
	"Seventeen", "Eighteen", "Nineteen",
}
var tens = []string{
	"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
}
var thousands = []string{"", "Thousand", "Million", "Billion"}

func convertChunk(value int) string {
	if value == 0 {
		return ""
	}
	if value < 20 {
		return ones[value]
	}
	if value < 100 {
		tensPart := tens[value/10]
		onesPart := ones[value%10]
		if onesPart == "" {
			return tensPart
		}
		return tensPart + " " + onesPart
	}
	hundreds := ones[value/100]
	remainder := convertChunk(value % 100)
	if remainder == "" {
		return hundreds + " Hundred"
	}
	return hundreds + " Hundred " + remainder
}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	parts := make([]string, 0)
	chunkIndex := 0
	for num > 0 {
		chunk := num % 1000
		if chunk != 0 {
			chunkWords := convertChunk(chunk)
			if thousands[chunkIndex] != "" {
				chunkWords += " " + thousands[chunkIndex]
			}
			parts = append(parts, chunkWords)
		}
		num /= 1000
		chunkIndex++
	}

	for left, right := 0, len(parts)-1; left < right; left, right = left+1, right-1 {
		parts[left], parts[right] = parts[right], parts[left]
	}
	result := ""
	for i, part := range parts {
		if i > 0 {
			result += " "
		}
		result += part
	}
	return result
}
