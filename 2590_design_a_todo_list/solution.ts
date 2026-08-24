// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

export class TodoList {
    constructor() {
    this.nextID = 1;
    this.tasks = new Map();
    this.users = new Map();
}
    addTask(userId: number, taskDescription: string, dueDate: number, tags: string[]): number {
    const id = this.nextID++;
    this.tasks.set(id, {
        id,
        description: taskDescription,
        dueDate,
        userId,
        tags: new Set(tags),
        done: false,
    });
    if (!this.users.has(userId)) this.users.set(userId, []);
    this.users.get(userId).push(id);
    return id;
}
    getAllTasks(userId: number): string[] {
    if (!this.users.has(userId)) return [];
    const ids = this.users.get(userId).slice();
    ids.sort((a, b) => this.tasks.get(a).dueDate - this.tasks.get(b).dueDate);
    const ans = [];
    for (const id of ids) {
        if (!this.tasks.get(id).done) ans.push(this.tasks.get(id).description);
    }
    return ans;
}
    getTasksForTag(userId: number, tag: string): string[] {
    if (!this.users.has(userId)) return [];
    const ids = this.users.get(userId).slice();
    ids.sort((a, b) => this.tasks.get(a).dueDate - this.tasks.get(b).dueDate);
    const ans = [];
    for (const id of ids) {
        const tk = this.tasks.get(id);
        if (!tk.done && tk.tags.has(tag)) ans.push(tk.description);
    }
    return ans;
}
    completeTask(userId: number, taskId: number): void {
    const tk = this.tasks.get(taskId);
    if (!tk || tk.userId !== userId || tk.done) return;
    tk.done = true;
}
}
