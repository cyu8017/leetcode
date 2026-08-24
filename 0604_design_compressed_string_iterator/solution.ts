// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

export class StringIterator {
    constructor(compressedString: string) {
    this.chars = [];
    this.counts = [];
    this.index = 0;
    let i = 0;
    const n = compressedString.length;
    while (i < n) {
        const ch = compressedString[i++];
        let j = i;
        while (j < n && compressedString[j] >= "0" && compressedString[j] <= "9") ++j;
        this.chars.push(ch);
        this.counts.push(Number(compressedString.substring(i, j)));
        i = j;
    }
}
    next(): string {
    if (!this.hasNext()) return " ";
    const ch = this.chars[this.index];
    this.counts[this.index] -= 1;
    if (this.counts[this.index] === 0) ++this.index;
    return ch;
}
    hasNext(): boolean {
    return this.index < this.chars.length;
}
}
