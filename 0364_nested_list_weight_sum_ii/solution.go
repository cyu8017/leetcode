// LeetCode 0364 - Nested List Weight Sum II
// https://leetcode.com/problems/nested-list-weight-sum-ii/

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
	weighted := make([][2]int, 0)

	var dfs func([]*NestedInteger, int)
	dfs = func(items []*NestedInteger, depth int) {
		for _, item := range items {
			if item.IsInteger() {
				weighted = append(weighted, [2]int{item.GetInteger(), depth})
			} else {
				dfs(item.GetList(), depth+1)
			}
		}
	}

	dfs(nestedList, 1)
	if len(weighted) == 0 {
		return 0
	}

	maxDepth := 0
	for _, entry := range weighted {
		if entry[1] > maxDepth {
			maxDepth = entry[1]
		}
	}

	total := 0
	for _, entry := range weighted {
		total += entry[0] * (maxDepth - entry[1] + 1)
	}

	return total
}
