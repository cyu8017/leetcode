// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

export class EventManager {
    constructor(events: any) {
    this.sl = [];
    this.d = new Map();
    for (const e of events) {
        const eventId = e[0], priority = e[1];
        this.sl.push([-priority, eventId]);
        this.d.set(eventId, priority);
    }
    this._sort();
}
    _sort(): any {
    this.sl.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
}
    updatePriority(eventId: any, newPriority: any): any {
    const old = this.d.get(eventId);
    this.sl = this.sl.filter(x => !(x[0] === -old && x[1] === eventId));
    this.sl.push([-newPriority, eventId]);
    this.d.set(eventId, newPriority);
    this._sort();
}
    pollHighest(): any {
    if (!this.sl.length) return -1;
    const top = this.sl.shift();
    const eventId = top[1];
    this.d.delete(eventId);
    return eventId;
}
}
