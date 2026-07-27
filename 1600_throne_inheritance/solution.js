// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance {
    /**
     * @param {string} kingName
     */
    constructor(kingName) {
        this.king = kingName;
        this.children = new Map();
        this.dead = new Set();
    }

    /**
     * @param {string} parentName
     * @param {string} childName
     * @return {null}
     */
    birth(parentName, childName) {
        if (!this.children.has(parentName)) this.children.set(parentName, []);
        this.children.get(parentName).push(childName);
        return null;
    }

    /**
     * @param {string} name
     * @return {null}
     */
    death(name) {
        this.dead.add(name);
        return null;
    }

    /**
     * @return {string[]}
     */
    getInheritanceOrder() {
        const order = [];
        const visit = (name) => {
            if (!this.dead.has(name)) order.push(name);
            for (const child of this.children.get(name) || []) visit(child);
        };
        visit(this.king);
        return order;
    }
}

module.exports = { ThroneInheritance };
