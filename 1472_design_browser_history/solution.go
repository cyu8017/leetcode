// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

type BrowserHistory struct {
	history []string
	index   int
}

func Constructor(homepage string) BrowserHistory {
	return BrowserHistory{history: []string{homepage}, index: 0}
}

func (this *BrowserHistory) Visit(url string) {
	this.history = this.history[:this.index+1]
	this.history = append(this.history, url)
	this.index++
}

func (this *BrowserHistory) Back(steps int) string {
	this.index -= steps
	if this.index < 0 {
		this.index = 0
	}
	return this.history[this.index]
}

func (this *BrowserHistory) Forward(steps int) string {
	this.index += steps
	if this.index >= len(this.history) {
		this.index = len(this.history) - 1
	}
	return this.history[this.index]
}
