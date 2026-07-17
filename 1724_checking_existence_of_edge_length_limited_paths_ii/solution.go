// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

import "sort"

type DistanceLimitedPathsExist struct {
	weights  []int
	versions [][]int
}

func Constructor(n int, edgeList [][]int) DistanceLimitedPathsExist {
	edges := make([][3]int, len(edgeList))
	for i, edge := range edgeList {
		edges[i] = [3]int{edge[2], edge[0], edge[1]}
	}
	sort.Slice(edges, func(i, j int) bool {
		if edges[i][0] != edges[j][0] {
			return edges[i][0] < edges[j][0]
		}
		if edges[i][1] != edges[j][1] {
			return edges[i][1] < edges[j][1]
		}
		return edges[i][2] < edges[j][2]
	})
	parent := make([]int, n)
	size := make([]int, n)
	for i := range parent {
		parent[i] = i
		size[i] = 1
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	obj := DistanceLimitedPathsExist{}
	i := 0
	for i < len(edges) {
		weight := edges[i][0]
		for i < len(edges) && edges[i][0] == weight {
			ra, rb := find(edges[i][1]), find(edges[i][2])
			if ra != rb {
				if size[ra] < size[rb] {
					ra, rb = rb, ra
				}
				parent[rb] = ra
				size[ra] += size[rb]
			}
			i++
		}
		snapshot := make([]int, n)
		copy(snapshot, parent)
		obj.weights = append(obj.weights, weight)
		obj.versions = append(obj.versions, snapshot)
	}
	return obj
}

func (this *DistanceLimitedPathsExist) Query(p int, q int, limit int) bool {
	idx := sort.SearchInts(this.weights, limit) - 1
	if idx < 0 {
		return p == q
	}
	parent := this.versions[idx]
	rp := p
	for parent[rp] != rp {
		rp = parent[rp]
	}
	rq := q
	for parent[rq] != rq {
		rq = parent[rq]
	}
	return rp == rq
}
