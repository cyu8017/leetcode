// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

type LUPrefix struct {
	uploaded []bool
	longest  int
}

func Constructor(n int) LUPrefix {
	return LUPrefix{uploaded: make([]bool, n+2)}
}

func (this *LUPrefix) Upload(video int) {
	this.uploaded[video] = true
	for this.uploaded[this.longest+1] {
		this.longest++
	}
}

func (this *LUPrefix) Longest() int {
	return this.longest
}
