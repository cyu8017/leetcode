// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

export class EventEmitter {
    constructor() {
    this.handlers = new Map();
}
    subscribe(eventName: any, callback: any): any {
    if (!this.handlers.has(eventName)) this.handlers.set(eventName, []);
    const list = this.handlers.get(eventName);
    list.push(callback);
    return {
        unsubscribe: () => {
            const idx = list.indexOf(callback);
            if (idx >= 0) list.splice(idx, 1);
        },
    };
}
    emit(eventName: any, args: any = []): any {
    const list = this.handlers.get(eventName) || [];
    return list.map((cb) => cb(...args));
}
}
