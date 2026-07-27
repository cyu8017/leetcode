"use strict";
// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/
Object.defineProperty(exports, "__esModule", { value: true });
exports.ThroneInheritance = void 0;
class ThroneInheritance {
    constructor(kingName) {
        this.children = new Map();
        this.dead = new Set();
        this.king = kingName;
    }
    birth(parentName, childName) {
        if (!this.children.has(parentName))
            this.children.set(parentName, []);
        this.children.get(parentName).push(childName);
        return null;
    }
    death(name) {
        this.dead.add(name);
        return null;
    }
    getInheritanceOrder() {
        const order = [];
        const visit = (name) => {
            if (!this.dead.has(name))
                order.push(name);
            for (const child of this.children.get(name) || [])
                visit(child);
        };
        visit(this.king);
        return order;
    }
}
exports.ThroneInheritance = ThroneInheritance;
