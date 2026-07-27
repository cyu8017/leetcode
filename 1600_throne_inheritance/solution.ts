// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

export class ThroneInheritance {
    private readonly king: string;
    private readonly children = new Map<string, string[]>();
    private readonly dead = new Set<string>();

    constructor(kingName: string) {
        this.king = kingName;
    }

    birth(parentName: string, childName: string): null {
        if (!this.children.has(parentName)) this.children.set(parentName, []);
        this.children.get(parentName)!.push(childName);
        return null;
    }

    death(name: string): null {
        this.dead.add(name);
        return null;
    }

    getInheritanceOrder(): string[] {
        const order: string[] = [];
        const visit = (name: string): void => {
            if (!this.dead.has(name)) order.push(name);
            for (const child of this.children.get(name) || []) visit(child);
        };
        visit(this.king);
        return order;
    }
}
