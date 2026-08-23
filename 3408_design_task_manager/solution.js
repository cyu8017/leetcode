// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

class TaskManager {
    /**
     * @param {number[][]} tasks
     */
    constructor(tasks) {
        this.pri = new Map();
        this.user = new Map();
        this.h = [];
        for (const t of tasks) this.add(t[0], t[1], t[2]);
    }

    /**
     * @param {number} userId
     * @param {number} taskId
     * @param {number} priority
     * @return {void}
     */
    add(userId, taskId, priority) {
        this.pri.set(taskId, priority);
        this.user.set(taskId, userId);
        this.h.push([priority, taskId, userId]);
    }

    /**
     * @param {number} taskId
     * @param {number} newPriority
     * @return {void}
     */
    edit(taskId, newPriority) {
        this.pri.set(taskId, newPriority);
        this.h.push([newPriority, taskId, this.user.get(taskId)]);
    }

    /**
     * @param {number} taskId
     * @return {void}
     */
    rmv(taskId) {
        this.pri.delete(taskId);
        this.user.delete(taskId);
    }

    /**
     * @return {number}
     */
    execTop() {
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
