// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

export class SORTracker {
    constructor() {
        this.best = []; // min-heap by score, then max name
        this.rest = []; // max-heap by score, then min name
        this.k = 0;
    }

    _cmpBest(a: any, b: any): any {
        if (a.score !== b.score) return a.score - b.score;
        return b.name < a.name ? -1 : b.name > a.name ? 1 : 0;
    }

    _cmpRest(a: any, b: any): any {
        if (a.score !== b.score) return b.score - a.score;
        return a.name < b.name ? -1 : a.name > b.name ? 1 : 0;
    }

    _push(heap: any, item: any, cmp: any): any {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (cmp(heap[p], heap[i]) <= 0) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    }

    _pop(heap: any, cmp: any): any {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1, r = l + 1, s = i;
                if (l < heap.length && cmp(heap[l], heap[s]) < 0) s = l;
                if (r < heap.length && cmp(heap[r], heap[s]) < 0) s = r;
                if (s === i) break;
                [heap[s], heap[i]] = [heap[i], heap[s]];
                i = s;
            }
        }
        return top;
    }

    add(name: any, score: any): any {
        this._push(this.best, {name, score}, this._cmpBest);
        if (this.best.length > this.k) this._push(this.rest, this._pop(this.best, this._cmpBest), this._cmpRest);
    }

    get(): any {
        this.k++;
        if (this.rest.length) this._push(this.best, this._pop(this.rest, this._cmpRest), this._cmpBest);
        return this.best[0].name;
    }
}
