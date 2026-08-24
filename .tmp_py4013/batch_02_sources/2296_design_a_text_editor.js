// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

var TextEditor = function() {
    this.left = [];
    this.right = [];
};

TextEditor.prototype.suffix = function() {
    const start = Math.max(0, this.left.length - 10);
    return this.left.slice(start).join('');
};

TextEditor.prototype.addText = function(text) {
    for (const c of text) this.left.push(c);
};

TextEditor.prototype.deleteText = function(k) {
    let deleted = 0;
    while (k > 0 && this.left.length) {
        this.left.pop();
        k--;
        deleted++;
    }
    return deleted;
};

TextEditor.prototype.cursorLeft = function(k) {
    while (k > 0 && this.left.length) {
        this.right.push(this.left.pop());
        k--;
    }
    return this.suffix();
};

TextEditor.prototype.cursorRight = function(k) {
    while (k > 0 && this.right.length) {
        this.left.push(this.right.pop());
        k--;
    }
    return this.suffix();
};
