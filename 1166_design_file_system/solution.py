# LeetCode 1166 - Design File System
# https://leetcode.com/problems/design-file-system/

class FileSystem:
    def __init__(self):
        self.paths: dict[str, int] = {"": -1}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False
        parent = path.rsplit("/", 1)[0]
        if parent not in self.paths:
            return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)
