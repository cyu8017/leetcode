// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

export function mostBooked(n: number, meetings: number[][]): number {
    meetings = meetings.slice().sort((a, b) => a[0] - b[0]);
    // min-heaps
    const free = [];
    const busy = []; // [endTime, room]
    const pushFree = (x) => {
        free.push(x);
        let i = free.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (free[p] <= free[i]) break;
            [free[p], free[i]] = [free[i], free[p]];
            i = p;
        }
    };
    const popFree = () => {
        const top = free[0];
        const last = free.pop();
        if (free.length > 0) {
            free[0] = last;
            let i = 0;
            while (true) {
                let s = i;
                const l = i * 2 + 1, r = i * 2 + 2;
                if (l < free.length && free[l] < free[s]) s = l;
                if (r < free.length && free[r] < free[s]) s = r;
                if (s === i) break;
                [free[s], free[i]] = [free[i], free[s]];
                i = s;
            }
        }
        return top;
    };
    const cmpBusy = (a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1];
    const pushBusy = (x) => {
        busy.push(x);
        let i = busy.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (cmpBusy(busy[p], busy[i]) <= 0) break;
            [busy[p], busy[i]] = [busy[i], busy[p]];
            i = p;
        }
    };
    const popBusy = () => {
        const top = busy[0];
        const last = busy.pop();
        if (busy.length > 0) {
            busy[0] = last;
            let i = 0;
            while (true) {
                let s = i;
                const l = i * 2 + 1, r = i * 2 + 2;
                if (l < busy.length && cmpBusy(busy[l], busy[s]) < 0) s = l;
                if (r < busy.length && cmpBusy(busy[r], busy[s]) < 0) s = r;
                if (s === i) break;
                [busy[s], busy[i]] = [busy[i], busy[s]];
                i = s;
            }
        }
        return top;
    };
    for (let i = 0; i < n; i++) pushFree(i);
    const cnt = Array(n).fill(0);
    for (const m of meetings) {
        const start = m[0], end = m[1];
        while (busy.length > 0 && busy[0][0] <= start) {
            pushFree(popBusy()[1]);
        }
        const dur = end - start;
        let room, begin;
        if (free.length > 0) {
            room = popFree();
            begin = start;
        } else {
            const top = popBusy();
            begin = top[0];
            room = top[1];
        }
        pushBusy([begin + dur, room]);
        cnt[room]++;
    }
    let ans = 0;
    for (let i = 1; i < n; i++) if (cnt[i] > cnt[ans]) ans = i;
    return ans;
}
