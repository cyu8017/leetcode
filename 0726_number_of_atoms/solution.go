// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

import (
	"sort"
	"strconv"
)

func countOfAtoms(formula string) string {
	stack := []map[string]int{{}}
	i, n := 0, len(formula)
	for i < n {
		if formula[i] == '(' {
			stack = append(stack, map[string]int{})
			i++
		} else if formula[i] == ')' {
			i++
			start := i
			for i < n && formula[i] >= '0' && formula[i] <= '9' {
				i++
			}
			mult := 1
			if start < i {
				mult, _ = strconv.Atoi(formula[start:i])
			}
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for atom, count := range top {
				stack[len(stack)-1][atom] += count * mult
			}
		} else {
			start := i
			i++
			for i < n && formula[i] >= 'a' && formula[i] <= 'z' {
				i++
			}
			atom := formula[start:i]
			start = i
			for i < n && formula[i] >= '0' && formula[i] <= '9' {
				i++
			}
			count := 1
			if start < i {
				count, _ = strconv.Atoi(formula[start:i])
			}
			stack[len(stack)-1][atom] += count
		}
	}
	counts := stack[0]
	atoms := make([]string, 0, len(counts))
	for atom := range counts {
		atoms = append(atoms, atom)
	}
	sort.Strings(atoms)
	out := ""
	for _, atom := range atoms {
		out += atom
		if counts[atom] > 1 {
			out += strconv.Itoa(counts[atom])
		}
	}
	return out
}
