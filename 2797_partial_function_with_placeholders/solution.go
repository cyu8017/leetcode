// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

func partial(fn func(...int) int, args []interface{}) func(...int) int {
	return func(rest ...int) int {
		full := make([]int, 0, len(args)+len(rest))
		ri := 0
		for _, a := range args {
			if a == nil {
				if ri < len(rest) {
					full = append(full, rest[ri])
					ri++
				}
			} else if v, ok := a.(int); ok {
				full = append(full, v)
			}
		}
		full = append(full, rest[ri:]...)
		return fn(full...)
	}
}
