// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

class FileSharing {
    private var owners = [Int: Set<Int>]()
    private var chunks = [Int: Set<Int>]()
    private var free = [Int]()
    private var nextId = 1

    init(_ m: Int) {}

    func join(_ ownedChunks: [Int]) -> Int {
        let user: Int
        if free.isEmpty {
            user = nextId
            nextId += 1
        } else {
            free.sort()
            user = free.removeFirst()
        }
        chunks[user] = Set(ownedChunks)
        for chunk in ownedChunks {
            owners[chunk, default: []].insert(user)
        }
        return user
    }

    func leave(_ userID: Int) {
        guard let owned = chunks.removeValue(forKey: userID) else { return }
        for chunk in owned {
            owners[chunk]?.remove(userID)
        }
        free.append(userID)
    }

    func request(_ userID: Int, _ chunkID: Int) -> [Int] {
        let users = (owners[chunkID] ?? []).sorted()
        if !users.isEmpty {
            chunks[userID, default: []].insert(chunkID)
            owners[chunkID, default: []].insert(userID)
        }
        return users
    }
}
