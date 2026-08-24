// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

export class TextEditor {
    constructor() {
    this.left = [];
    this.right = [];
}
    suffix(): any {
    const start = Math.max(0, this.left.length - 10);
    return this.left.slice(start).join('');
}
    addText(text: any): any {
    for (const c of text) this.left.push(c);
}
    deleteText(k: any): any {
    let deleted = 0;
    while (k > 0 && this.left.length) {
        this.left.pop();
        k--;
        deleted++;
    }
    return deleted;
}
    cursorLeft(k: any): any {
    while (k > 0 && this.left.length) {
        this.right.push(this.left.pop());
        k--;
    }
    return this.suffix();
}
    cursorRight(k: any): any {
    while (k > 0 && this.right.length) {
        this.left.push(this.right.pop());
        k--;
    }
    return this.suffix();
}
}
