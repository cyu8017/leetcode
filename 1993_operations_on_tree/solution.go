// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

type LockingTree struct {
	locked   []int
	parent   []int
	children [][]int
}

func Constructor(parent []int) LockingTree {
	n := len(parent)
	lt := LockingTree{
		locked:   make([]int, n),
		parent:   parent,
		children: make([][]int, n),
	}
	for i := range lt.locked {
		lt.locked[i] = -1
	}
	for son := 1; son < n; son++ {
		fa := parent[son]
		lt.children[fa] = append(lt.children[fa], son)
	}
	return lt
}

func (this *LockingTree) Lock(num int, user int) bool {
	if this.locked[num] == -1 {
		this.locked[num] = user
		return true
	}
	return false
}

func (this *LockingTree) Unlock(num int, user int) bool {
	if this.locked[num] == user {
		this.locked[num] = -1
		return true
	}
	return false
}

func (this *LockingTree) Upgrade(num int, user int) bool {
	x := num
	for x != -1 {
		if this.locked[x] != -1 {
			return false
		}
		x = this.parent[x]
	}
	find := false
	var dfs func(u int)
	dfs = func(u int) {
		for _, v := range this.children[u] {
			if this.locked[v] != -1 {
				this.locked[v] = -1
				find = true
			}
			dfs(v)
		}
	}
	dfs(num)
	if !find {
		return false
	}
	this.locked[num] = user
	return true
}
