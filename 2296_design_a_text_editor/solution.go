// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

type TextEditor struct {
	left, right []byte
}

func Constructor() TextEditor {
	return TextEditor{}
}

func (this *TextEditor) AddText(text string) {
	this.left = append(this.left, text...)
}

func (this *TextEditor) DeleteText(k int) int {
	deleted := 0
	for k > 0 && len(this.left) > 0 {
		this.left = this.left[:len(this.left)-1]
		k--
		deleted++
	}
	return deleted
}

func (this *TextEditor) CursorLeft(k int) string {
	for k > 0 && len(this.left) > 0 {
		this.right = append(this.right, this.left[len(this.left)-1])
		this.left = this.left[:len(this.left)-1]
		k--
	}
	return this.suffix()
}

func (this *TextEditor) CursorRight(k int) string {
	for k > 0 && len(this.right) > 0 {
		this.left = append(this.left, this.right[len(this.right)-1])
		this.right = this.right[:len(this.right)-1]
		k--
	}
	return this.suffix()
}

func (this *TextEditor) suffix() string {
	start := len(this.left) - 10
	if start < 0 {
		start = 0
	}
	return string(this.left[start:])
}
