// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

class SQL {
    constructor(names, columns) {
        this.tables = new Map();
        this.nextID = new Map();
        for (const name of names) {
            this.tables.set(name, []);
            this.nextID.set(name, 1);
        }
    }
    ins(name, row) {
        if (!this.tables.has(name)) return false;
        const id = this.nextID.get(name);
        this.nextID.set(name, id + 1);
        const full = [String(id), ...row];
        this.tables.get(name).push(full);
        return true;
    }
    rmv(name, rowId) {
        const rows = this.tables.get(name);
        for (let i = 0; i < rows.length; i++) {
            if (parseInt(rows[i][0], 10) === rowId) {
                rows.splice(i, 1);
                return;
            }
        }
    }
    sel(name, rowId, columnId) {
        for (const r of this.tables.get(name)) {
            if (parseInt(r[0], 10) === rowId) {
                if (columnId < 1 || columnId >= r.length) return "<null>";
                return r[columnId];
            }
        }
        return "<null>";
    }
    exp(name) {
        const ans = [];
        for (const r of this.tables.get(name)) {
            ans.push(r.join(','));
        }
        return ans;
    }
}
