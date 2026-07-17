// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

func minOperationsToFlip(expression string) int {
	index := 0

	min2 := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	min3 := func(a, b, c int) int {
		return min2(a, min2(b, c))
	}

	combine := func(left [3]int, op byte, right [3]int) [3]int {
		leftVal, leftToZero, leftToOne := left[0], left[1], left[2]
		rightVal, rightToZero, rightToOne := right[0], right[1], right[2]
		if op == '&' {
			andVal := leftVal & rightVal
			andToZero := min2(leftToZero, leftToOne+rightToZero)
			andToOne := leftToOne + rightToOne
			orToZero := leftToZero + rightToZero
			orToOne := min3(leftToOne, leftToZero+rightToOne, rightToZero+leftToOne)
			val := andVal
			toZero := min2(andToZero, 1+orToZero)
			toOne := min2(andToOne, 1+orToOne)
			return [3]int{val, toZero, toOne}
		}
		orVal := leftVal | rightVal
		orToZero := leftToZero + rightToZero
		orToOne := min3(leftToOne, leftToZero+rightToOne, rightToZero+leftToOne)
		andToZero := min2(leftToZero, leftToOne+rightToZero)
		andToOne := leftToOne + rightToOne
		val := orVal
		toZero := min2(orToZero, 1+andToZero)
		toOne := min2(orToOne, 1+andToOne)
		return [3]int{val, toZero, toOne}
	}

	var parseExpr func() [3]int
	var parseFactor func() [3]int

	parseFactor = func() [3]int {
		if expression[index] == '0' || expression[index] == '1' {
			value := int(expression[index] - '0')
			index++
			toZero := 0
			toOne := 1
			if value == 1 {
				toZero = 1
				toOne = 0
			}
			return [3]int{value, toZero, toOne}
		}
		index++
		node := parseExpr()
		index++
		return node
	}

	parseExpr = func() [3]int {
		node := parseFactor()
		for index < len(expression) && (expression[index] == '&' || expression[index] == '|') {
			op := expression[index]
			index++
			node = combine(node, op, parseFactor())
		}
		return node
	}

	result := parseExpr()
	if result[0] == 0 {
		return result[2]
	}
	return result[1]
}
