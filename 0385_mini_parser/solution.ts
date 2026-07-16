// LeetCode 0385 - Mini Parser
export class NestedInteger {
    private integer: number | null;
    private list: NestedInteger[];

    constructor(value: number | null = null) {
        this.integer = value;
        this.list = [];
    }

    isInteger(): boolean {
        return this.integer !== null;
    }

    getInteger(): number {
        return this.integer ?? 0;
    }

    getList(): NestedInteger[] {
        return this.list;
    }
}

export class Solution {
    deserialize(s: string): NestedInteger {
        if (s[0] !== "[") {
            return new NestedInteger(Number(s));
        }

        const stack: NestedInteger[] = [];
        let current: NestedInteger | null = null;
        let index = 0;
        let negative = false;
        let number = 0;
        let hasNumber = false;

        while (index < s.length) {
            const char = s[index];
            if (char === "[") {
                const item = new NestedInteger();
                if (current) stack.push(current);
                current = item;
            } else if (char === "-") {
                negative = true;
            } else if (char >= "0" && char <= "9") {
                number = number * 10 + Number(char);
                hasNumber = true;
            } else if (char === "," || char === "]") {
                if (hasNumber) {
                    current!.getList().push(new NestedInteger(negative ? -number : number));
                    number = 0;
                    negative = false;
                    hasNumber = false;
                }
                if (char === "]") {
                    if (!stack.length) return current!;
                    const parent = stack.pop()!;
                    parent.getList().push(current!);
                    current = parent;
                }
            }
            index += 1;
        }

        return current ?? new NestedInteger();
    }
}
