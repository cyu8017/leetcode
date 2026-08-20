"use strict";
// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/
// @ts-nocheck
Object.defineProperty(exports, "__esModule", { value: true });
exports.FileSharing = void 0;
class FileSharing {
    constructor(m) {
        this.owners = new Map();
        this.chunks = new Map();
        this.free = [];
        this.nextId = 1;
    }
    join(ownedChunks) {
        let user;
        if (this.free.length) {
            this.free.sort((a, b) => a - b);
            user = this.free.shift();
        }
        else {
            user = this.nextId++;
        }
        const set = new Set(ownedChunks);
        this.chunks.set(user, set);
        for (const chunk of ownedChunks) {
            if (!this.owners.has(chunk))
                this.owners.set(chunk, new Set());
            this.owners.get(chunk).add(user);
        }
        return user;
    }
    leave(userID) {
        const owned = this.chunks.get(userID) || [];
        for (const chunk of owned) {
            const set = this.owners.get(chunk);
            if (set)
                set.delete(userID);
        }
        this.chunks.delete(userID);
        this.free.push(userID);
        return null;
    }
    request(userID, chunkID) {
        const users = [...(this.owners.get(chunkID) || [])].sort((a, b) => a - b);
        if (users.length) {
            this.chunks.get(userID).add(chunkID);
            if (!this.owners.has(chunkID))
                this.owners.set(chunkID, new Set());
            this.owners.get(chunkID).add(userID);
        }
        return users;
    }
}
exports.FileSharing = FileSharing;
