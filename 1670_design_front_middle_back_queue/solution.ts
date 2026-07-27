// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

export class FrontMiddleBackQueue {
    private l: number[] = [];
    private r: number[] = [];

    private _bal(): void {
        while (this.l.length > this.r.length + 1) this.r.unshift(this.l.pop()!);
        while (this.r.length > this.l.length) this.l.push(this.r.shift()!);
    }

    pushFront(val: number): null {
        this.l.unshift(val);
        this._bal();
        return null;
    }

    pushMiddle(val: number): null {
        if (this.l.length > this.r.length) this.r.unshift(this.l.pop()!);
        this.l.push(val);
        return null;
    }

    pushBack(val: number): null {
        this.r.push(val);
        this._bal();
        return null;
    }

    popFront(): number {
        if (!this.l.length) return -1;
        const v = this.l.shift()!;
        this._bal();
        return v;
    }

    popMiddle(): number {
        if (!this.l.length) return -1;
        const v = this.l.pop()!;
        this._bal();
        return v;
    }

    popBack(): number {
        if (!this.l.length) return -1;
        const v = this.r.length ? this.r.pop()! : this.l.pop()!;
        this._bal();
        return v;
    }
}
