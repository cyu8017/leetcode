// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

export class TaskManager {
    constructor(tasks: any) {
        this.pri = new Map();
        this.user = new Map();
        this.h = [];
        for (const t of tasks) this.add(t[0], t[1], t[2]);
    }

    add(userId: any, taskId: any, priority: any): any {
        this.pri.set(taskId, priority);
        this.user.set(taskId, userId);
        this.h.push([priority, taskId, userId]);
    }

    edit(taskId: any, newPriority: any): any {
        this.pri.set(taskId, newPriority);
        this.h.push([newPriority, taskId, this.user.get(taskId)]);
    }

    rmv(taskId: any): any {
        this.pri.delete(taskId);
        this.user.delete(taskId);
    }

    execTop(): any {
        this.h.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
        while (this.h.length) {
            const top = this.h.pop();
            const p = this.pri.get(top[1]);
            if (p !== undefined && p === top[0] && this.user.get(top[1]) === top[2]) {
                this.pri.delete(top[1]);
                const uid = this.user.get(top[1]);
                this.user.delete(top[1]);
                return uid;
            }
        }
        return -1;
    }
}
