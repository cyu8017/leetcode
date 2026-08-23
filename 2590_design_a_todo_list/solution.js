// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

var TodoList = function() {
    this.nextID = 1;
    this.tasks = new Map();
    this.users = new Map();
};

/** 
 * @param {number} userId 
 * @param {string} taskDescription 
 * @param {number} dueDate 
 * @param {string[]} tags
 * @return {number}
 */
TodoList.prototype.addTask = function(userId, taskDescription, dueDate, tags) {
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
};

/** 
 * @param {number} userId
 * @return {string[]}
 */
TodoList.prototype.getAllTasks = function(userId) {
    if (!this.users.has(userId)) return [];
    const ids = this.users.get(userId).slice();
    ids.sort((a, b) => this.tasks.get(a).dueDate - this.tasks.get(b).dueDate);
    const ans = [];
    for (const id of ids) {
        if (!this.tasks.get(id).done) ans.push(this.tasks.get(id).description);
    }
    return ans;
};

/** 
 * @param {number} userId 
 * @param {string} tag
 * @return {string[]}
 */
TodoList.prototype.getTasksForTag = function(userId, tag) {
    if (!this.users.has(userId)) return [];
    const ids = this.users.get(userId).slice();
    ids.sort((a, b) => this.tasks.get(a).dueDate - this.tasks.get(b).dueDate);
    const ans = [];
    for (const id of ids) {
        const tk = this.tasks.get(id);
        if (!tk.done && tk.tags.has(tag)) ans.push(tk.description);
    }
    return ans;
};

/** 
 * @param {number} userId 
 * @param {number} taskId
 * @return {void}
 */
TodoList.prototype.completeTask = function(userId, taskId) {
    const tk = this.tasks.get(taskId);
    if (!tk || tk.userId !== userId || tk.done) return;
    tk.done = true;
};
