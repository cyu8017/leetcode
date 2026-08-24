// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

export class ATM {
    constructor() {
    this.cnt = [0, 0, 0, 0, 0];
    this.vals = [20, 50, 100, 200, 500];
}
    deposit(banknotesCount: number[]): void {
    for (let i = 0; i < 5; i++) this.cnt[i] += banknotesCount[i];
}
    withdraw(amount: number): number[] {
    const take = [0, 0, 0, 0, 0];
    let remain = amount;
    const tmp = this.cnt.slice();
    for (let i = 4; i >= 0; i--) {
        let need = Math.floor(remain / this.vals[i]);
        if (need > tmp[i]) need = tmp[i];
        take[i] = need;
        remain -= need * this.vals[i];
    }
    if (remain !== 0) return [-1];
    for (let i = 0; i < 5; i++) this.cnt[i] -= take[i];
    return take;
}
}
