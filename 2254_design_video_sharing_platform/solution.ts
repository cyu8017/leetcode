// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

export class MinHeap {
    constructor(cmp: any) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
    _up(i: any): any {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
}
    _down(i: any): any {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
}
    push(x: any): any { this.a.push(x); this._up(this.a.length - 1); }
    pop(): any {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
}
    size(): any { return this.a.length; }
}

export class VideoSharingPlatform {
    constructor() {
    this.nextID = 0;
    this.free = new MinHeap();
    this.videos = new Map();
    this.views = new Map();
    this.likes = new Map();
    this.dislikes = new Map();
}
    upload(video: string): number {
    const id = this.free.size() ? this.free.pop() : this.nextID++;
    this.videos.set(id, video);
    this.views.set(id, 0);
    this.likes.set(id, 0);
    this.dislikes.set(id, 0);
    return id;
}
    remove(videoId: number): void {
    if (!this.videos.has(videoId)) return;
    this.videos.delete(videoId);
    this.views.delete(videoId);
    this.likes.delete(videoId);
    this.dislikes.delete(videoId);
    this.free.push(videoId);
}
    watch(videoId: number, startMinute: number, endMinute: number): string {
    const v = this.videos.get(videoId);
    if (v === undefined) return '-1';
    this.views.set(videoId, this.views.get(videoId) + 1);
    if (startMinute >= v.length) return '';
    endMinute = Math.min(endMinute, v.length - 1);
    return v.substring(startMinute, endMinute + 1);
}
    like(videoId: number): void {
    if (this.videos.has(videoId)) this.likes.set(videoId, this.likes.get(videoId) + 1);
}
    dislike(videoId: number): void {
    if (this.videos.has(videoId)) this.dislikes.set(videoId, this.dislikes.get(videoId) + 1);
}
    getLikesAndDislikes(videoId: number): number[] {
    if (!this.videos.has(videoId)) return [-1];
    return [this.likes.get(videoId), this.dislikes.get(videoId)];
}
    getViews(videoId: number): number {
    if (!this.videos.has(videoId)) return -1;
    return this.views.get(videoId);
}
}
