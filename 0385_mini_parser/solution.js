// LeetCode 0385 - Mini Parser
class NestedInteger {
    constructor(value = null) {
        this.integer = value;
        this.list = [];
    }

    isInteger() {
        return this.integer !== null;
    }

    getInteger() {
        return this.integer ?? 0;
    }

    getList() {
        return this.list;
    }
}

class Solution {
    deserialize(s) {
        if (s[0] !== "[") {
            return new NestedInteger(Number(s));
        }

        const stack = [];
        let current = null;
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
                    current.getList().push(new NestedInteger(negative ? -number : number));
                    number = 0;
                    negative = false;
                    hasNumber = false;
                }
                if (char === "]") {
                    if (!stack.length) return current;
                    const parent = stack.pop();
                    parent.getList().push(current);
                    current = parent;
                }
            }
            index += 1;
        }

        return current ?? new NestedInteger();
    }
}

module.exports = { NestedInteger, Solution };
