// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

export class LUPrefix {
    constructor(n: number) {
    this.uploaded = Array(n + 2).fill(false);
    this.prefixLen = 0;
}
    upload(video: number): void {
    this.uploaded[video] = true;
    while (this.uploaded[this.prefixLen + 1]) this.prefixLen++;
}
    longest(): number {
    return this.prefixLen;
}
}
