// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

import "sort"

type SnapshotArray struct {
	snapID int
	data   [][][2]int
}

func Constructor(length int) SnapshotArray {
	data := make([][][2]int, length)
	for i := range data {
		data[i] = [][2]int{{0, 0}}
	}
	return SnapshotArray{data: data}
}

func (this *SnapshotArray) Set(index int, val int) {
	hist := this.data[index]
	if hist[len(hist)-1][0] == this.snapID {
		hist[len(hist)-1][1] = val
	} else {
		this.data[index] = append(hist, [2]int{this.snapID, val})
	}
}

func (this *SnapshotArray) Snap() int {
	id := this.snapID
	this.snapID++
	return id
}

func (this *SnapshotArray) Get(index int, snap_id int) int {
	hist := this.data[index]
	i := sort.Search(len(hist), func(i int) bool {
		return hist[i][0] > snap_id
	}) - 1
	return hist[i][1]
}
