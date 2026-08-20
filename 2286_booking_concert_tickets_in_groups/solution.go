// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

type BookMyShow struct {
	n, m int
	tree []node
}

type node struct {
	sum int64
	mx  int64
}

func Constructor(n int, m int) BookMyShow {
	b := BookMyShow{n: n, m: m, tree: make([]node, 4*n)}
	b.build(1, 0, n-1)
	return b
}

func (this *BookMyShow) build(idx, l, r int) {
	if l == r {
		this.tree[idx] = node{sum: int64(this.m), mx: int64(this.m)}
		return
	}
	mid := (l + r) / 2
	this.build(idx*2, l, mid)
	this.build(idx*2+1, mid+1, r)
	this.pull(idx)
}

func (this *BookMyShow) pull(idx int) {
	this.tree[idx].sum = this.tree[idx*2].sum + this.tree[idx*2+1].sum
	this.tree[idx].mx = this.tree[idx*2].mx
	if this.tree[idx*2+1].mx > this.tree[idx].mx {
		this.tree[idx].mx = this.tree[idx*2+1].mx
	}
}

func (this *BookMyShow) update(idx, l, r, pos int, val int64) {
	if l == r {
		this.tree[idx].sum = val
		this.tree[idx].mx = val
		return
	}
	mid := (l + r) / 2
	if pos <= mid {
		this.update(idx*2, l, mid, pos, val)
	} else {
		this.update(idx*2+1, mid+1, r, pos, val)
	}
	this.pull(idx)
}

func (this *BookMyShow) querySum(idx, l, r, ql, qr int) int64 {
	if qr < l || r < ql {
		return 0
	}
	if ql <= l && r <= qr {
		return this.tree[idx].sum
	}
	mid := (l + r) / 2
	return this.querySum(idx*2, l, mid, ql, qr) + this.querySum(idx*2+1, mid+1, r, ql, qr)
}

func (this *BookMyShow) findFirst(idx, l, r int, maxRow int, k int64) int {
	if l > maxRow || this.tree[idx].mx < k {
		return -1
	}
	if l == r {
		return l
	}
	mid := (l + r) / 2
	left := this.findFirst(idx*2, l, mid, maxRow, k)
	if left != -1 {
		return left
	}
	return this.findFirst(idx*2+1, mid+1, r, maxRow, k)
}

func (this *BookMyShow) Gather(k int, maxRow int) []int {
	row := this.findFirst(1, 0, this.n-1, maxRow, int64(k))
	if row == -1 {
		return []int{}
	}
	remain := this.querySum(1, 0, this.n-1, row, row)
	seat := int(int64(this.m) - remain)
	this.update(1, 0, this.n-1, row, remain-int64(k))
	return []int{row, seat}
}

func (this *BookMyShow) Scatter(k int, maxRow int) bool {
	if this.querySum(1, 0, this.n-1, 0, maxRow) < int64(k) {
		return false
	}
	need := int64(k)
	for row := 0; row <= maxRow && need > 0; row++ {
		remain := this.querySum(1, 0, this.n-1, row, row)
		if remain == 0 {
			continue
		}
		take := remain
		if take > need {
			take = need
		}
		this.update(1, 0, this.n-1, row, remain-take)
		need -= take
	}
	return true
}
