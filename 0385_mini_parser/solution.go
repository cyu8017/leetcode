// LeetCode 0385 - Mini Parser
// https://leetcode.com/problems/mini-parser/

import "strconv"

type NestedInteger struct {
	integer *int
	list    []*NestedInteger
}

func (n NestedInteger) IsInteger() bool {
	return n.integer != nil
}

func (n NestedInteger) GetInteger() int {
	if n.integer == nil {
		return 0
	}
	return *n.integer
}

func (n NestedInteger) GetList() []*NestedInteger {
	return n.list
}

func deserialize(s string) *NestedInteger {
	if len(s) == 0 || s[0] != '[' {
		value, _ := strconv.Atoi(s)
		return &NestedInteger{integer: &value}
	}

	stack := make([]*NestedInteger, 0)
	var current *NestedInteger
	index := 0
	negative := false
	number := 0
	hasNumber := false

	for index < len(s) {
		ch := s[index]
		switch {
		case ch == '[':
			item := &NestedInteger{}
			if current != nil {
				stack = append(stack, current)
			}
			current = item
		case ch == '-':
			negative = true
		case ch >= '0' && ch <= '9':
			number = number*10 + int(ch-'0')
			hasNumber = true
		case ch == ',' || ch == ']':
			if hasNumber {
				value := number
				if negative {
					value = -number
				}
				current.list = append(current.list, &NestedInteger{integer: &value})
				number = 0
				negative = false
				hasNumber = false
			}
			if ch == ']' {
				if len(stack) == 0 {
					return current
				}
				parent := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				parent.list = append(parent.list, current)
				current = parent
			}
		}
		index++
	}

	if current == nil {
		return &NestedInteger{}
	}
	return current
}
