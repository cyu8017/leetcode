// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

import (
	"strconv"
	"strings"
)

type Codec struct{}

func (this *Codec) Encode(strs []string) string {
	var encoded strings.Builder
	for _, text := range strs {
		encoded.WriteString(strconv.Itoa(len(text)))
		encoded.WriteByte('#')
		encoded.WriteString(text)
	}
	return encoded.String()
}

func (this *Codec) Decode(encoded string) []string {
	result := make([]string, 0)
	index := 0
	for index < len(encoded) {
		delimiter := strings.IndexByte(encoded[index:], '#') + index
		length, _ := strconv.Atoi(encoded[index:delimiter])
		start := delimiter + 1
		result = append(result, encoded[start:start+length])
		index = start + length
	}
	return result
}
