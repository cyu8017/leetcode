// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

function MinHeap(cmp) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
MinHeap.prototype._up = function(i) {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
MinHeap.prototype._down = function(i) {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
};
MinHeap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
MinHeap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
MinHeap.prototype.size = function() { return this.a.length; };

var VideoSharingPlatform = function() {
    this.nextID = 0;
    this.free = new MinHeap();
    this.videos = new Map();
    this.views = new Map();
    this.likes = new Map();
    this.dislikes = new Map();
};

/** 
 * @param {string} video
 * @return {number}
 */
VideoSharingPlatform.prototype.upload = function(video) {
    const id = this.free.size() ? this.free.pop() : this.nextID++;
    this.videos.set(id, video);
    this.views.set(id, 0);
    this.likes.set(id, 0);
    this.dislikes.set(id, 0);
    return id;
};

/** 
 * @param {number} videoId
 * @return {void}
 */
VideoSharingPlatform.prototype.remove = function(videoId) {
    if (!this.videos.has(videoId)) return;
    this.videos.delete(videoId);
    this.views.delete(videoId);
    this.likes.delete(videoId);
    this.dislikes.delete(videoId);
    this.free.push(videoId);
};

/** 
 * @param {number} videoId 
 * @param {number} startMinute 
 * @param {number} endMinute
 * @return {string}
 */
VideoSharingPlatform.prototype.watch = function(videoId, startMinute, endMinute) {
    const v = this.videos.get(videoId);
    if (v === undefined) return '-1';
    this.views.set(videoId, this.views.get(videoId) + 1);
    if (startMinute >= v.length) return '';
    endMinute = Math.min(endMinute, v.length - 1);
    return v.substring(startMinute, endMinute + 1);
};

/** 
 * @param {number} videoId
 * @return {void}
 */
VideoSharingPlatform.prototype.like = function(videoId) {
    if (this.videos.has(videoId)) this.likes.set(videoId, this.likes.get(videoId) + 1);
};

/** 
 * @param {number} videoId
 * @return {void}
 */
VideoSharingPlatform.prototype.dislike = function(videoId) {
    if (this.videos.has(videoId)) this.dislikes.set(videoId, this.dislikes.get(videoId) + 1);
};

/** 
 * @param {number} videoId
 * @return {number[]}
 */
VideoSharingPlatform.prototype.getLikesAndDislikes = function(videoId) {
    if (!this.videos.has(videoId)) return [-1];
    return [this.likes.get(videoId), this.dislikes.get(videoId)];
};

/** 
 * @param {number} videoId
 * @return {number}
 */
VideoSharingPlatform.prototype.getViews = function(videoId) {
    if (!this.videos.has(videoId)) return -1;
    return this.views.get(videoId);
};
