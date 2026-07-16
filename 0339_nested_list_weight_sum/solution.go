// LeetCode 0339 - Nested List Weight Sum
// https://leetcode.com/problems/nested-list-weight-sum/

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

func depthSum(nestedList []*NestedInteger) int {
	total := 0

	var dfs func(items []*NestedInteger, depth int)
	dfs = func(items []*NestedInteger, depth int) {
		for _, item := range items {
			if item.IsInteger() {
				total += item.GetInteger() * depth
			} else {
				dfs(item.GetList(), depth+1)
			}
		}
	}

	dfs(nestedList, 1)
	return total
}
